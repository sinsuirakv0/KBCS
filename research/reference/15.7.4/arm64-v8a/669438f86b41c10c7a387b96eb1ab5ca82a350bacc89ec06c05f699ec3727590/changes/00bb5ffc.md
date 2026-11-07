# `00bb5ef0` → `00bb5ffc` の本文差分

[旧版の関数資料](../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5ef0.md) · [新版の関数資料](../functions/00bb5/00bb5ffc.md) · [変更一覧](README.md)

行番号は各疑似コード原本に対応します。`-` は旧版、`+` は新版の抜粋です。

~~~diff
@@ -36,5 +36,5 @@
       if (param_6 == 0) {
         *param_1 = (int)DAT_002b2708;
-joined_r0x00bb60c4:
+joined_r0x00bb61d0:
         if (param_5 == '\0') {
           return;
@@ -44,5 +44,5 @@
         }
         if (param_5 != '\x01') goto LAB_00bb62b8;
-        goto joined_r0x00bb62b0;
+        goto joined_r0x00bb63bc;
       }
       if (param_6 != 1) goto LAB_00bb62b8;
@@ -213,5 +213,5 @@
     if (param_6 == 0) {
       *param_1 = (int)DAT_002b2bf8;
-      goto joined_r0x00bb60c4;
+      goto joined_r0x00bb61d0;
     }
     if (param_6 != 1) goto LAB_00bb62b8;
@@ -297,5 +297,5 @@
   }
   *(undefined2 *)((long)param_1 + 1) = uVar5;
-joined_r0x00bb62b0:
+joined_r0x00bb63bc:
   if (!bVar4) {
     _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc(param_2,0,1,0x20);
~~~
