
var Module = typeof Module !== 'undefined' ? Module : {};

if (!Module.expectedDataFileDownloads) {
  Module.expectedDataFileDownloads = 0;
  Module.finishedDataFileDownloads = 0;
}
Module.expectedDataFileDownloads++;
(function() {
 var loadPackage = function(metadata) {

    var PACKAGE_PATH;
    if (typeof window === 'object') {
      PACKAGE_PATH = window['encodeURIComponent'](window.location.pathname.toString().substring(0, window.location.pathname.toString().lastIndexOf('/')) + '/');
    } else if (typeof location !== 'undefined') {
      // worker
      PACKAGE_PATH = encodeURIComponent(location.pathname.toString().substring(0, location.pathname.toString().lastIndexOf('/')) + '/');
    } else {
      throw 'using preloaded data can only be done on a web page or in a web worker';
    }
    var PACKAGE_NAME = 'pythonhome.data';
    var REMOTE_PACKAGE_BASE = 'pythonhome.data';
    if (typeof Module['locateFilePackage'] === 'function' && !Module['locateFile']) {
      Module['locateFile'] = Module['locateFilePackage'];
      err('warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)');
    }
    var REMOTE_PACKAGE_NAME = Module['locateFile'] ? Module['locateFile'](REMOTE_PACKAGE_BASE, '') : REMOTE_PACKAGE_BASE;
  
    var REMOTE_PACKAGE_SIZE = metadata.remote_package_size;
    var PACKAGE_UUID = metadata.package_uuid;
  
    function fetchRemotePackage(packageName, packageSize, callback, errback) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', packageName, true);
      xhr.responseType = 'arraybuffer';
      xhr.onprogress = function(event) {
        var url = packageName;
        var size = packageSize;
        if (event.total) size = event.total;
        if (event.loaded) {
          if (!xhr.addedTotal) {
            xhr.addedTotal = true;
            if (!Module.dataFileDownloads) Module.dataFileDownloads = {};
            Module.dataFileDownloads[url] = {
              loaded: event.loaded,
              total: size
            };
          } else {
            Module.dataFileDownloads[url].loaded = event.loaded;
          }
          var total = 0;
          var loaded = 0;
          var num = 0;
          for (var download in Module.dataFileDownloads) {
          var data = Module.dataFileDownloads[download];
            total += data.total;
            loaded += data.loaded;
            num++;
          }
          total = Math.ceil(total * Module.expectedDataFileDownloads/num);
          if (Module['setStatus']) Module['setStatus']('Downloading data... (' + loaded + '/' + total + ')');
        } else if (!Module.dataFileDownloads) {
          if (Module['setStatus']) Module['setStatus']('Downloading data...');
        }
      };
      xhr.onerror = function(event) {
        throw new Error("NetworkError for: " + packageName);
      }
      xhr.onload = function(event) {
        if (xhr.status == 200 || xhr.status == 304 || xhr.status == 206 || (xhr.status == 0 && xhr.response)) { // file URLs can return 0
          var packageData = xhr.response;
          callback(packageData);
        } else {
          throw new Error(xhr.statusText + " : " + xhr.responseURL);
        }
      };
      xhr.send(null);
    };

    function handleError(error) {
      console.error('package error:', error);
    };
  
  function runWithFS() {

    function assert(check, msg) {
      if (!check) throw msg + new Error().stack;
    }
Module['FS_createPath']('/', 'lib', true, true);
Module['FS_createPath']('/lib', 'python2.7', true, true);
Module['FS_createPath']('/lib/python2.7', 'importlib', true, true);
Module['FS_createPath']('/lib/python2.7', 'xml', true, true);
Module['FS_createPath']('/lib/python2.7/xml', 'etree', true, true);
Module['FS_createPath']('/lib/python2.7', 'json', true, true);
Module['FS_createPath']('/lib/python2.7', 'encodings', true, true);

    function DataRequest(start, end, audio) {
      this.start = start;
      this.end = end;
      this.audio = audio;
    }
    DataRequest.prototype = {
      requests: {},
      open: function(mode, name) {
        this.name = name;
        this.requests[name] = this;
        Module['addRunDependency']('fp ' + this.name);
      },
      send: function() {},
      onload: function() {
        var byteArray = this.byteArray.subarray(this.start, this.end);
        this.finish(byteArray);
      },
      finish: function(byteArray) {
        var that = this;

        Module['FS_createDataFile'](this.name, null, byteArray, true, true, true); // canOwn this data in the filesystem, it is a slide into the heap that will never change
        Module['removeRunDependency']('fp ' + that.name);

        this.requests[this.name] = null;
      }
    };

        var files = metadata.files;
        for (var i = 0; i < files.length; ++i) {
          new DataRequest(files[i].start, files[i].end, files[i].audio).open('GET', files[i].filename);
        }

  
      var indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;
      var IDB_RO = "readonly";
      var IDB_RW = "readwrite";
      var DB_NAME = "EM_PRELOAD_CACHE";
      var DB_VERSION = 1;
      var METADATA_STORE_NAME = 'METADATA';
      var PACKAGE_STORE_NAME = 'PACKAGES';
      function openDatabase(callback, errback) {
        try {
          var openRequest = indexedDB.open(DB_NAME, DB_VERSION);
        } catch (e) {
          return errback(e);
        }
        openRequest.onupgradeneeded = function(event) {
          var db = event.target.result;

          if(db.objectStoreNames.contains(PACKAGE_STORE_NAME)) {
            db.deleteObjectStore(PACKAGE_STORE_NAME);
          }
          var packages = db.createObjectStore(PACKAGE_STORE_NAME);

          if(db.objectStoreNames.contains(METADATA_STORE_NAME)) {
            db.deleteObjectStore(METADATA_STORE_NAME);
          }
          var metadata = db.createObjectStore(METADATA_STORE_NAME);
        };
        openRequest.onsuccess = function(event) {
          var db = event.target.result;
          callback(db);
        };
        openRequest.onerror = function(error) {
          errback(error);
        };
      };

      // This is needed as chromium has a limit on per-entry files in IndexedDB
      // https://cs.chromium.org/chromium/src/content/renderer/indexed_db/webidbdatabase_impl.cc?type=cs&sq=package:chromium&g=0&l=177
      // https://cs.chromium.org/chromium/src/out/Debug/gen/third_party/blink/public/mojom/indexeddb/indexeddb.mojom.h?type=cs&sq=package:chromium&g=0&l=60
      // We set the chunk size to 64MB to stay well-below the limit
      var CHUNK_SIZE = 64 * 1024 * 1024;

      function cacheRemotePackage(
        db,
        packageName,
        packageData,
        packageMeta,
        callback,
        errback
      ) {
        var transactionPackages = db.transaction([PACKAGE_STORE_NAME], IDB_RW);
        var packages = transactionPackages.objectStore(PACKAGE_STORE_NAME);
        var chunkSliceStart = 0;
        var nextChunkSliceStart = 0;
        var chunkCount = Math.ceil(packageData.byteLength / CHUNK_SIZE);
        var finishedChunks = 0;
        for (var chunkId = 0; chunkId < chunkCount; chunkId++) {
          nextChunkSliceStart += CHUNK_SIZE;
          var putPackageRequest = packages.put(
            packageData.slice(chunkSliceStart, nextChunkSliceStart),
            'package/' + packageName + '/' + chunkId
          );
          chunkSliceStart = nextChunkSliceStart;
          putPackageRequest.onsuccess = function(event) {
            finishedChunks++;
            if (finishedChunks == chunkCount) {
              var transaction_metadata = db.transaction(
                [METADATA_STORE_NAME],
                IDB_RW
              );
              var metadata = transaction_metadata.objectStore(METADATA_STORE_NAME);
              var putMetadataRequest = metadata.put(
                {
                  uuid: packageMeta.uuid,
                  chunkCount: chunkCount
                },
                'metadata/' + packageName
              );
              putMetadataRequest.onsuccess = function(event) {
                callback(packageData);
              };
              putMetadataRequest.onerror = function(error) {
                errback(error);
              };
            }
          };
          putPackageRequest.onerror = function(error) {
            errback(error);
          };
        }
      }

      /* Check if there's a cached package, and if so whether it's the latest available */
      function checkCachedPackage(db, packageName, callback, errback) {
        var transaction = db.transaction([METADATA_STORE_NAME], IDB_RO);
        var metadata = transaction.objectStore(METADATA_STORE_NAME);
        var getRequest = metadata.get('metadata/' + packageName);
        getRequest.onsuccess = function(event) {
          var result = event.target.result;
          if (!result) {
            return callback(false, null);
          } else {
            return callback(PACKAGE_UUID === result.uuid, result);
          }
        };
        getRequest.onerror = function(error) {
          errback(error);
        };
      }

      function fetchCachedPackage(db, packageName, metadata, callback, errback) {
        var transaction = db.transaction([PACKAGE_STORE_NAME], IDB_RO);
        var packages = transaction.objectStore(PACKAGE_STORE_NAME);

        var chunksDone = 0;
        var totalSize = 0;
        var chunks = new Array(metadata.chunkCount);

        for (var chunkId = 0; chunkId < metadata.chunkCount; chunkId++) {
          var getRequest = packages.get('package/' + packageName + '/' + chunkId);
          getRequest.onsuccess = function(event) {
            // If there's only 1 chunk, there's nothing to concatenate it with so we can just return it now
            if (metadata.chunkCount == 1) {
              callback(event.target.result);
            } else {
              chunksDone++;
              totalSize += event.target.result.byteLength;
              chunks.push(event.target.result);
              if (chunksDone == metadata.chunkCount) {
                if (chunksDone == 1) {
                  callback(event.target.result);
                } else {
                  var tempTyped = new Uint8Array(totalSize);
                  var byteOffset = 0;
                  for (var chunkId in chunks) {
                    var buffer = chunks[chunkId];
                    tempTyped.set(new Uint8Array(buffer), byteOffset);
                    byteOffset += buffer.byteLength;
                    buffer = undefined;
                  }
                  chunks = undefined;
                  callback(tempTyped.buffer);
                  tempTyped = undefined;
                }
              }
            }
          };
          getRequest.onerror = function(error) {
            errback(error);
          };
        }
      }
    
    function processPackageData(arrayBuffer) {
      Module.finishedDataFileDownloads++;
      assert(arrayBuffer, 'Loading data file failed.');
      assert(arrayBuffer instanceof ArrayBuffer, 'bad input to processPackageData');
      var byteArray = new Uint8Array(arrayBuffer);
      var curr;
      
        // Reuse the bytearray from the XHR as the source for file reads.
        DataRequest.prototype.byteArray = byteArray;
  
          var files = metadata.files;
          for (var i = 0; i < files.length; ++i) {
            DataRequest.prototype.requests[files[i].filename].onload();
          }
              Module['removeRunDependency']('datafile_pythonhome.data');

    };
    Module['addRunDependency']('datafile_pythonhome.data');
  
    if (!Module.preloadResults) Module.preloadResults = {};
  
      function preloadFallback(error) {
        console.error(error);
        console.error('falling back to default preload behavior');
        fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE, processPackageData, handleError);
      };

      openDatabase(
        function(db) {
          checkCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME,
            function(useCached, metadata) {
              Module.preloadResults[PACKAGE_NAME] = {fromCache: useCached};
              if (useCached) {
                fetchCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME, metadata, processPackageData, preloadFallback);
              } else {
                fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE,
                  function(packageData) {
                    cacheRemotePackage(db, PACKAGE_PATH + PACKAGE_NAME, packageData, {uuid:PACKAGE_UUID}, processPackageData,
                      function(error) {
                        console.error(error);
                        processPackageData(packageData);
                      });
                  }
                , preloadFallback);
              }
            }
          , preloadFallback);
        }
      , preloadFallback);

      if (Module['setStatus']) Module['setStatus']('Downloading...');
    
  }
  if (Module['calledRun']) {
    runWithFS();
  } else {
    if (!Module['preRun']) Module['preRun'] = [];
    Module["preRun"].push(runWithFS); // FS is not initialized yet, wait for it
  }

 }
 loadPackage({"files": [{"start": 0, "audio": 0, "end": 35991, "filename": "/lib/python2.7/zipfile.pyo"}, {"start": 35991, "audio": 0, "end": 38587, "filename": "/lib/python2.7/genericpath.pyo"}, {"start": 38587, "audio": 0, "end": 43774, "filename": "/lib/python2.7/repr.pyo"}, {"start": 43774, "audio": 0, "end": 52228, "filename": "/lib/python2.7/UserDict.pyo"}, {"start": 52228, "audio": 0, "end": 66802, "filename": "/lib/python2.7/tempfile.pyo"}, {"start": 66802, "audio": 0, "end": 79059, "filename": "/lib/python2.7/sre_compile.pyo"}, {"start": 79059, "audio": 0, "end": 82429, "filename": "/lib/python2.7/chunk.pyo"}, {"start": 82429, "audio": 0, "end": 84776, "filename": "/lib/python2.7/fnmatch.pyo"}, {"start": 84776, "audio": 0, "end": 86593, "filename": "/lib/python2.7/keyword.pyo"}, {"start": 86593, "audio": 0, "end": 93164, "filename": "/lib/python2.7/re.pyo"}, {"start": 93164, "audio": 0, "end": 119070, "filename": "/lib/python2.7/platform.pyo"}, {"start": 119070, "audio": 0, "end": 132030, "filename": "/lib/python2.7/shutil.pyo"}, {"start": 132030, "audio": 0, "end": 146543, "filename": "/lib/python2.7/gettext.pyo"}, {"start": 146543, "audio": 0, "end": 171219, "filename": "/lib/python2.7/inspect.pyo"}, {"start": 171219, "audio": 0, "end": 178649, "filename": "/lib/python2.7/traceback.pyo"}, {"start": 178649, "audio": 0, "end": 196654, "filename": "/lib/python2.7/webbrowser.pyo"}, {"start": 196654, "audio": 0, "end": 216716, "filename": "/lib/python2.7/_abcoll.pyo"}, {"start": 216716, "audio": 0, "end": 223010, "filename": "/lib/python2.7/StringIO.pyo"}, {"start": 223010, "audio": 0, "end": 229983, "filename": "/lib/python2.7/shlex.pyo"}, {"start": 229983, "audio": 0, "end": 290005, "filename": "/lib/python2.7/tarfile.pyo"}, {"start": 290005, "audio": 0, "end": 304704, "filename": "/lib/python2.7/sysconfig.pyo"}, {"start": 304704, "audio": 0, "end": 307341, "filename": "/lib/python2.7/linecache.pyo"}, {"start": 307341, "audio": 0, "end": 316930, "filename": "/lib/python2.7/copy.pyo"}, {"start": 316930, "audio": 0, "end": 327895, "filename": "/lib/python2.7/tokenize.pyo"}, {"start": 327895, "audio": 0, "end": 331227, "filename": "/lib/python2.7/colorsys.pyo"}, {"start": 331227, "audio": 0, "end": 333427, "filename": "/lib/python2.7/__future__.pyo"}, {"start": 333427, "audio": 0, "end": 335982, "filename": "/lib/python2.7/stat.pyo"}, {"start": 335982, "audio": 0, "end": 349499, "filename": "/lib/python2.7/sunau.pyo"}, {"start": 349499, "audio": 0, "end": 349732, "filename": "/lib/python2.7/struct.pyo"}, {"start": 349732, "audio": 0, "end": 354518, "filename": "/lib/python2.7/functools.pyo"}, {"start": 354518, "audio": 0, "end": 366005, "filename": "/lib/python2.7/heapq.pyo"}, {"start": 366005, "audio": 0, "end": 420597, "filename": "/lib/python2.7/argparse.pyo"}, {"start": 420597, "audio": 0, "end": 423116, "filename": "/lib/python2.7/types.pyo"}, {"start": 423116, "audio": 0, "end": 429466, "filename": "/lib/python2.7/hashlib.pyo"}, {"start": 429466, "audio": 0, "end": 448710, "filename": "/lib/python2.7/_sysconfigdata.pyo"}, {"start": 448710, "audio": 0, "end": 454174, "filename": "/lib/python2.7/textwrap.pyo"}, {"start": 454174, "audio": 0, "end": 460283, "filename": "/lib/python2.7/sre_constants.pyo"}, {"start": 460283, "audio": 0, "end": 480355, "filename": "/lib/python2.7/codecs.pyo"}, {"start": 480355, "audio": 0, "end": 490113, "filename": "/lib/python2.7/warnings.pyo"}, {"start": 490113, "audio": 0, "end": 502801, "filename": "/lib/python2.7/string.pyo"}, {"start": 502801, "audio": 0, "end": 509986, "filename": "/lib/python2.7/ast.pyo"}, {"start": 509986, "audio": 0, "end": 517436, "filename": "/lib/python2.7/base64.pyo"}, {"start": 517436, "audio": 0, "end": 527653, "filename": "/lib/python2.7/urlparse.pyo"}, {"start": 527653, "audio": 0, "end": 542652, "filename": "/lib/python2.7/os.pyo"}, {"start": 542652, "audio": 0, "end": 548621, "filename": "/lib/python2.7/opcode.pyo"}, {"start": 548621, "audio": 0, "end": 566126, "filename": "/lib/python2.7/collections.pyo"}, {"start": 566126, "audio": 0, "end": 593755, "filename": "/lib/python2.7/difflib.pyo"}, {"start": 593755, "audio": 0, "end": 606556, "filename": "/lib/python2.7/socket.pyo"}, {"start": 606556, "audio": 0, "end": 623459, "filename": "/lib/python2.7/random.pyo"}, {"start": 623459, "audio": 0, "end": 626536, "filename": "/lib/python2.7/dummy_thread.pyo"}, {"start": 626536, "audio": 0, "end": 632142, "filename": "/lib/python2.7/dis.pyo"}, {"start": 632142, "audio": 0, "end": 636428, "filename": "/lib/python2.7/copy_reg.pyo"}, {"start": 636428, "audio": 0, "end": 648798, "filename": "/lib/python2.7/weakref.pyo"}, {"start": 648798, "audio": 0, "end": 662462, "filename": "/lib/python2.7/site.pyo"}, {"start": 662462, "audio": 0, "end": 682207, "filename": "/lib/python2.7/sre_parse.pyo"}, {"start": 682207, "audio": 0, "end": 724936, "filename": "/lib/python2.7/urllib.pyo"}, {"start": 724936, "audio": 0, "end": 775167, "filename": "/lib/python2.7/locale.pyo"}, {"start": 775167, "audio": 0, "end": 777235, "filename": "/lib/python2.7/io.pyo"}, {"start": 777235, "audio": 0, "end": 810374, "filename": "/lib/python2.7/pickle.pyo"}, {"start": 810374, "audio": 0, "end": 814102, "filename": "/lib/python2.7/token.pyo"}, {"start": 814102, "audio": 0, "end": 827671, "filename": "/lib/python2.7/wave.pyo"}, {"start": 827671, "audio": 0, "end": 831475, "filename": "/lib/python2.7/abc.pyo"}, {"start": 831475, "audio": 0, "end": 840037, "filename": "/lib/python2.7/posixpath.pyo"}, {"start": 840037, "audio": 0, "end": 842333, "filename": "/lib/python2.7/glob.pyo"}, {"start": 842333, "audio": 0, "end": 851723, "filename": "/lib/python2.7/_weakrefset.pyo"}, {"start": 851723, "audio": 0, "end": 854727, "filename": "/lib/python2.7/contextlib.pyo"}, {"start": 854727, "audio": 0, "end": 855857, "filename": "/lib/python2.7/importlib/__init__.pyo"}, {"start": 855857, "audio": 0, "end": 856401, "filename": "/lib/python2.7/xml/__init__.pyo"}, {"start": 856401, "audio": 0, "end": 856524, "filename": "/lib/python2.7/xml/etree/__init__.pyo"}, {"start": 856524, "audio": 0, "end": 890349, "filename": "/lib/python2.7/xml/etree/ElementTree.pyo"}, {"start": 890349, "audio": 0, "end": 897817, "filename": "/lib/python2.7/xml/etree/ElementPath.pyo"}, {"start": 897817, "audio": 0, "end": 906609, "filename": "/lib/python2.7/json/encoder.pyo"}, {"start": 906609, "audio": 0, "end": 909385, "filename": "/lib/python2.7/json/__init__.pyo"}, {"start": 909385, "audio": 0, "end": 917175, "filename": "/lib/python2.7/json/decoder.pyo"}, {"start": 917175, "audio": 0, "end": 919342, "filename": "/lib/python2.7/json/scanner.pyo"}, {"start": 919342, "audio": 0, "end": 921349, "filename": "/lib/python2.7/encodings/raw_unicode_escape.pyo"}, {"start": 921349, "audio": 0, "end": 924759, "filename": "/lib/python2.7/encodings/zlib_codec.pyo"}, {"start": 924759, "audio": 0, "end": 926826, "filename": "/lib/python2.7/encodings/ascii.pyo"}, {"start": 926826, "audio": 0, "end": 929647, "filename": "/lib/python2.7/encodings/__init__.pyo"}, {"start": 929647, "audio": 0, "end": 931455, "filename": "/lib/python2.7/encodings/utf_32_be.pyo"}, {"start": 931455, "audio": 0, "end": 933550, "filename": "/lib/python2.7/encodings/latin_1.pyo"}, {"start": 933550, "audio": 0, "end": 936089, "filename": "/lib/python2.7/encodings/hex_codec.pyo"}, {"start": 936089, "audio": 0, "end": 944256, "filename": "/lib/python2.7/encodings/aliases.pyo"}, {"start": 944256, "audio": 0, "end": 946020, "filename": "/lib/python2.7/encodings/utf_8.pyo"}], "remote_package_size": 946020, "package_uuid": "86e88338-b7c9-4749-ada1-f45839730fff"});

})();
