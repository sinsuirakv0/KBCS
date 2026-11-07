# `00bac998` → `00bacaa4` の本文差分

[旧版の関数資料](../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bac998.md) · [新版の関数資料](../functions/00bac/00bacaa4.md) · [変更一覧](README.md)

行番号は各疑似コード原本に対応します。`-` は旧版、`+` は新版の抜粋です。

~~~diff
@@ -54,5 +54,5 @@
         if (uVar6 == 0xed) {
           uVar1 = uVar7 & 0xe0;
-joined_r0x00bacb04:
+joined_r0x00bacc10:
           if (uVar1 != 0x80) {
             return (bool)2;
@@ -62,5 +62,5 @@
           if (uVar6 != 0xe0) {
             uVar1 = uVar7 & 0xc0;
-            goto joined_r0x00bacb04;
+            goto joined_r0x00bacc10;
           }
           if ((uVar7 & 0xe0) != 0xa0) {
@@ -89,5 +89,5 @@
         if (uVar6 == 0xf4) {
           uVar1 = uVar7 & 0xf0;
-joined_r0x00bacb54:
+joined_r0x00bacc60:
           if (uVar1 != 0x80) {
             return (bool)2;
@@ -97,5 +97,5 @@
           if (uVar6 != 0xf0) {
             uVar1 = uVar7 & 0xc0;
-            goto joined_r0x00bacb54;
+            goto joined_r0x00bacc60;
           }
           if (0x2f < uVar7 - 0x90) {
~~~
