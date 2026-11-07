# `00bbf9c4` → `00bbfad0` の本文差分

[旧版の関数資料](../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) · [新版の関数資料](../functions/00bbf/00bbfad0.md) · [変更一覧](README.md)

行番号は各疑似コード原本に対応します。`-` は旧版、`+` は新版の抜粋です。

~~~diff
@@ -114,5 +114,5 @@
       *param_1 = (long)(pbVar6 + 2);
       puVar1 = (undefined8 *)FUN_00bbd1fc(param_1);
-joined_r0x00bbfa60:
+joined_r0x00bbfb6c:
       if (puVar1 != (undefined8 *)0x0) {
         pcVar4 = (char *)*param_1;
@@ -172,5 +172,5 @@
     *param_1 = (long)(pbVar6 + 1);
     puVar1 = (undefined8 *)FUN_00bc2e00(param_1);
-    goto joined_r0x00bbfa60;
+    goto joined_r0x00bbfb6c;
   }
   puVar1 = (undefined8 *)FUN_00bbdd50(param_1);
~~~
