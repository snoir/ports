--- setup.py.orig	2020-12-17 15:45:24 UTC
+++ setup.py
@@ -42,7 +42,7 @@ def _data_files(path):
     for root, _, files in os.walk(path):
         if not files:
             continue
-        yield (os.path.join('/usr', root), [os.path.join(root, f) for f in files])
+        yield (os.path.join('/usr/local', root), [os.path.join(root, f) for f in files])
 
 
 def __package_files(directory):
