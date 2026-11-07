# `00bbdd50` → `00bbde5c` の本文差分

[旧版の関数資料](../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · [新版の関数資料](../functions/00bbd/00bbde5c.md) · [変更一覧](README.md)

行番号は各疑似コード原本に対応します。`-` は旧版、`+` は新版の抜粋です。

~~~diff
@@ -31,5 +31,5 @@
   local_58 = (undefined8 *)0x0;
   uVar5 = (long)pbVar6 - (long)pcVar12;
-  if (uVar5 == 0) goto code_r0x00bbe784;
+  if (uVar5 == 0) goto code_r0x00bbe890;
   cVar1 = *pcVar12;
   switch(cVar1) {
@@ -43,5 +43,5 @@
       uVar5 = FUN_00bc2e00(param_1);
       puVar3 = (undefined8 *)0x0;
-      if (uVar5 == 0) goto joined_r0x00bbee24;
+      if (uVar5 == 0) goto joined_r0x00bbef30;
                     /* try { // try from 00bbed08 to 00cbed0f has its CatchHandler @ 00bbee2c */
       pcVar12 = (char *)*param_1;
@@ -87,7 +87,7 @@
       puVar3 = (undefined8 *)FUN_00bd3c80(param_1,local_50,&local_28);
     }
-    goto joined_r0x00bbee24;
+    goto joined_r0x00bbef30;
   default:
-    goto code_r0x00bbe784;
+    goto code_r0x00bbe890;
   case 'C':
     *param_1 = (long)(pcVar12 + 1);
@@ -151,5 +151,5 @@
       return puVar3;
     default:
-      goto code_r0x00bbec64;
+      goto code_r0x00bbed70;
     case 'F':
                     /* try { // try from 00bbef1c to 00cbefb3 has its CatchHandler @ 00bbefb4 */
@@ -191,5 +191,5 @@
     case 'w':
     case 'x':
-      goto code_r0x00bbe858;
+      goto code_r0x00bbe964;
     case 'T':
     case 't':
@@ -267,7 +267,7 @@
       puVar3 = (undefined8 *)FUN_00bd1eec(param_1);
     }
-    goto joined_r0x00bbee24;
+    goto joined_r0x00bbef30;
   case 'F':
-    goto code_r0x00bbe858;
+    goto code_r0x00bbe964;
   case 'G':
                     /* try { // try from 00bbe570 to 00cbe57f has its CatchHandler @ 00bbee24 */
@@ -309,6 +309,6 @@
           (0x29 < (byte)pcVar12[uVar15 + 1] - 0x4f)) ||
          ((1L << ((ulong)((byte)pcVar12[uVar15 + 1] - 0x4f) & 0x3f) & 0x30100000001U) == 0))))))
-    goto code_r0x00bbde50;
-    goto code_r0x00bbe858;
+    goto code_r0x00bbdf5c;
+    goto code_r0x00bbe964;
   case 'M':
     *param_1 = (long)(pcVar12 + 1);
@@ -324,5 +324,5 @@
       }
     }
-    goto joined_r0x00bbee24;
+    goto joined_r0x00bbef30;
   case 'O':
     *param_1 = (long)(pcVar12 + 1);
@@ -387,5 +387,5 @@
       goto LAB_00bbe790;
     }
-    goto code_r0x00bbe784;
+    goto code_r0x00bbe890;
   case 'T':
     if (((uVar5 < 2) || (0x10 < (byte)pcVar12[1] - 0x65)) ||
@@ -405,11 +405,11 @@
       goto LAB_00bbece8;
     }
-code_r0x00bbe784:
+code_r0x00bbe890:
     puVar3 = (undefined8 *)FUN_00bd21a8(param_1);
-    goto joined_r0x00bbee24;
+    goto joined_r0x00bbef30;
   case 'U':
-code_r0x00bbde50:
+code_r0x00bbdf5c:
     puVar3 = (undefined8 *)FUN_00bd166c(param_1);
-joined_r0x00bbee24:
+joined_r0x00bbef30:
                     /* catch() { ... } // from try @ 00bbe570 with catch @ 00bbee24
                        catch() { ... } // from try @ 00bbe5b0 with catch @ 00bbee24
@@ -1052,11 +1052,11 @@
   puVar2[2] = pcVar12;
   puVar2[3] = uVar11;
-code_r0x00bbec64:
+code_r0x00bbed70:
                     /* try { // try from 00bbec6c to 00cbec8b has its CatchHandler @ 00bbee74 */
   return puVar2;
-code_r0x00bbe858:
+code_r0x00bbe964:
   puVar3 = (undefined8 *)FUN_00bd10c4(param_1);
-  goto joined_r0x00bbee24;
-}
-
-
+  goto joined_r0x00bbef30;
+}
+
+
~~~
