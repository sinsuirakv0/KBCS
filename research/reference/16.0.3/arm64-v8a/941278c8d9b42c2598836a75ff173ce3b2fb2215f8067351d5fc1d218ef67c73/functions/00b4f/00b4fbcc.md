# 00b4fbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b4fbcc",
  "name": "_ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject",
  "size": 4228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e055ed85758087ebe30cd791ffc5911349db7ae75094f940ec4195ac4a185969",
  "source_text_sha256": "e055ed85758087ebe30cd791ffc5911349db7ae75094f940ec4195ac4a185969"
}
~~~

## 呼び出し元

- [00c5bf40](../00c5b/00c5bf40.md)

## 呼び出し先

- [00b50c50](../00b50/00b50c50.md)
- [00b51e74](../00b51/00b51e74.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)
- [00c5c3f0](../00c5c/00c5c3f0.md)
- [00c5c440](../00c5c/00c5c440.md)
- [00c5c580](../00c5c/00c5c580.md)
- [00c5c590](../00c5c/00c5c590.md)

## 関連文字列（未確認候補）

~~~text
"%PG%dalvik/system/DexClassLoader"
"android/content/ContentResolver"
"android/content/Context"
"android/content/Intent"
"android/content/res/AssetFileDescriptor"
"android/content/res/Resources"
"android/database/Cursor"
"android/net/Uri"
"android/net/Uri$Builder"
"android/os/Bundle"
"android/os/ParcelFileDescriptor"
"app_resources_lib.jar"
"com/google/firebase/app/internal/cpp/JniResultCallback"
"com/google/firebase/app/internal/cpp/Log"
"java/io/File"
"java/io/FileOutputStream"
"java/lang/Boolean"
"java/lang/Byte"
"java/lang/Character"
"java/lang/Class"
"java/lang/Double"
"java/lang/Enum"
"java/lang/Float"
"java/lang/Integer"
"java/lang/Iterable"
"java/lang/Long"
"java/lang/Object"
"java/lang/Short"
"java/lang/String"
"java/lang/Throwable"
"java/net/URL"
"java/util/ArrayList"
"java/util/Date"
"java/util/HashMap"
"java/util/Iterator"
"java/util/List"
"java/util/Map"
"java/util/Set"
~~~

## 疑似コード / UTF-8 52903 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject(long *param_1,undefined8 param_2)

{
  undefined8 *__src;
  long lVar1;
  code *pcVar2;
  undefined *puVar3;
  undefined *puVar4;
  bool bVar5;
  char cVar6;
  int iVar7;
  ulong uVar8;
  undefined8 *puVar9;
  void *__dest;
  undefined4 uVar10;
  undefined8 uVar11;
  undefined8 *local_88;
  undefined8 *local_80;
  undefined8 *local_78;
  void *local_70;
  void *local_68;
  void *pvStack_60;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  if (DAT_01126e38 != 0) {
    DAT_01126e38 = DAT_01126e38 + 1;
    uVar10 = 1;
    goto LAB_00b50b48;
  }
  uVar8 = _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject();
  if ((uVar8 & 1) != 0) {
    if (DAT_011268f0 == 0) {
      DAT_011268f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                               (param_1,param_2,0,"java/util/ArrayList",0);
    }
    uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                      (param_1,DAT_011268f0,&PTR_s_<init>_00c90b10,3,&DAT_01126900,
                       "java/util/ArrayList");
    if ((uVar8 & 1) != 0) {
      if (DAT_01126920 == 0) {
        DAT_01126920 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (param_1,param_2,0,"android/content/res/AssetFileDescriptor",0);
      }
      uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                        (param_1,DAT_01126920,&PTR_s_getParcelFileDescriptor_00c90b58,1,
                         &DAT_01126930,"android/content/res/AssetFileDescriptor");
      if ((uVar8 & 1) != 0) {
        if (DAT_01126940 == 0) {
          DAT_01126940 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                   (param_1,param_2,0,"java/lang/Boolean",0);
        }
        uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                          (param_1,DAT_01126940,&PTR_s_<init>_00c90b70,2,&DAT_01126950,
                           "java/lang/Boolean");
        if ((uVar8 & 1) != 0) {
          if (DAT_01126968 == 0) {
            DAT_01126968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                     (param_1,param_2,0,"android/os/Bundle",0);
                    /* catch() { ... } // from try @ 00b4f538 with catch @ 00b4fd50 */
                    /* catch() { ... } // from try @ 00b4f518 with catch @ 00b4fd54 */
          }
                    /* catch() { ... } // from try @ 00b4f4e4 with catch @ 00b4fd64 */
                    /* catch() { ... } // from try @ 00b4f4c0 with catch @ 00b4fd68 */
                    /* catch() { ... } // from try @ 00b4f494 with catch @ 00b4fd78 */
          uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                            (param_1,DAT_01126968,&PTR_s_<init>_00c90ba0,9,&DAT_01126978,
                             "android/os/Bundle");
                    /* catch() { ... } // from try @ 00b4f474 with catch @ 00b4fd7c */
          if ((uVar8 & 1) != 0) {
            if (DAT_011269c8 == 0) {
                    /* catch() { ... } // from try @ 00b4f440 with catch @ 00b4fd8c */
                    /* catch() { ... } // from try @ 00b4f41c with catch @ 00b4fd90 */
                    /* catch() { ... } // from try @ 00b4f3f0 with catch @ 00b4fda0 */
                    /* catch() { ... } // from try @ 00b4f3d0 with catch @ 00b4fda4 */
              DAT_011269c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                       (param_1,param_2,0,"java/lang/Byte",0);
            }
                    /* catch() { ... } // from try @ 00b4f398 with catch @ 00b4fdb4 */
                    /* catch() { ... } // from try @ 00b4f374 with catch @ 00b4fdb8 */
                    /* catch() { ... } // from try @ 00b4c338 with catch @ 00b4fdc8
                       catch() { ... } // from try @ 00b4c3cc with catch @ 00b4fdc8 */
            uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                              (param_1,DAT_011269c8,&PTR_s_<init>_00c90c78,2,&DAT_011269d8,
                               "java/lang/Byte");
            if ((uVar8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4f544 with catch @ 00b4fddc */
              if (DAT_011269f0 == 0) {
                DAT_011269f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                         (param_1,param_2,0,"java/lang/Character",0);
              }
                    /* catch() { ... } // from try @ 00b4a4f8 with catch @ 00b4fe18 */
              uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                (param_1,DAT_011269f0,&PTR_s_<init>_00c90ca8,2,&DAT_01126a00,
                                 "java/lang/Character");
                    /* catch() { ... } // from try @ 00b4f3ac with catch @ 00b4fe2c
                       catch() { ... } // from try @ 00b4f454 with catch @ 00b4fe2c
                       catch() { ... } // from try @ 00b4f4f8 with catch @ 00b4fe2c */
              if ((uVar8 & 1) != 0) {
                if (DAT_01126a18 == 0) {
                    /* catch() { ... } // from try @ 00b4ad0c with catch @ 00b4fe4c */
                  DAT_01126a18 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                           (param_1,param_2,0,"java/lang/Class",0);
                }
                    /* catch() { ... } // from try @ 00b4f574 with catch @ 00b4fe64 */
                    /* catch() { ... } // from try @ 00b498b4 with catch @ 00b4fe68 */
                    /* catch() { ... } // from try @ 00b49674 with catch @ 00b4fe6c */
                    /* catch() { ... } // from try @ 00b49664 with catch @ 00b4fe70 */
                    /* catch() { ... } // from try @ 00b49380 with catch @ 00b4fe74 */
                    /* catch() { ... } // from try @ 00b49a98 with catch @ 00b4fe78 */
                uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                  (param_1,DAT_01126a18,&PTR_s_isArray_00c90cd8,2,&DAT_01126a28,
                                   "java/lang/Class");
                if ((uVar8 & 1) != 0) {
                  if (DAT_01126a40 == 0) {
                    /* catch() { ... } // from try @ 00b49a80 with catch @ 00b4fe94 */
                    /* catch() { ... } // from try @ 00b49a34 with catch @ 00b4fe98 */
                    /* catch() { ... } // from try @ 00b4a418 with catch @ 00b4fe9c */
                    DAT_01126a40 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                             (param_1,param_2,0,"android/content/ContentResolver",0)
                    ;
                    /* catch() { ... } // from try @ 00b49be4 with catch @ 00b4feb0 */
                    /* catch() { ... } // from try @ 00b493d0 with catch @ 00b4feb4
                       catch() { ... } // from try @ 00b49514 with catch @ 00b4feb4 */
                  }
                    /* catch() { ... } // from try @ 00b49ae8 with catch @ 00b4feb8 */
                    /* catch() { ... } // from try @ 00b4f950 with catch @ 00b4febc */
                    /* catch() { ... } // from try @ 00b4dc9c with catch @ 00b4fec0 */
                    /* catch() { ... } // from try @ 00b4dc90 with catch @ 00b4fed8 */
                  uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                    (param_1,DAT_01126a40,&PTR_s_openAssetFileDescriptor_00c90d08,2,
                                     &DAT_01126a50,"android/content/ContentResolver");
                  if ((uVar8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4dbcc with catch @ 00b4fee8 */
                    if (DAT_01126a68 == 0) {
                    /* catch() { ... } // from try @ 00b4dbc0 with catch @ 00b4ff00 */
                      DAT_01126a68 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                               (param_1,param_2,0,"android/content/Context",0);
                    }
                    /* catch() { ... } // from try @ 00b4d250 with catch @ 00b4ff14 */
                    /* catch() { ... } // from try @ 00b4aa8c with catch @ 00b4ff20 */
                    /* catch() { ... } // from try @ 00b4a2bc with catch @ 00b4ff24 */
                    /* catch() { ... } // from try @ 00b49e34 with catch @ 00b4ff2c */
                    uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                      (param_1,DAT_01126a68,&PTR_s_getFilesDir_00c90d38,3,
                                       &DAT_01126a78,"android/content/Context");
                    if ((uVar8 & 1) != 0) {
                      if (DAT_01126a98 == 0) {
                    /* catch() { ... } // from try @ 00b49e20 with catch @ 00b4ff58 */
                        DAT_01126a98 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                 (param_1,param_2,0,"android/database/Cursor",0);
                      }
                      uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                        (param_1,DAT_01126a98,&PTR_s_getColumnIndex_00c90d80,4,
                                         &DAT_01126aa8,"android/database/Cursor");
                      if ((uVar8 & 1) != 0) {
                        if (DAT_01126ad0 == 0) {
                          DAT_01126ad0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                   (param_1,param_2,0,"java/util/Date",0);
                        }
                    /* catch() { ... } // from try @ 00b49344 with catch @ 00b4ffd4 */
                        uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                          (param_1,DAT_01126ad0,&PTR_s_<init>_00c90de0,3,
                                           &DAT_01126ae0,"java/util/Date");
                        if ((uVar8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4ad28 with catch @ 00b4ffec
                       catch() { ... } // from try @ 00b4af00 with catch @ 00b4ffec */
                    /* catch() { ... } // from try @ 00b4aea8 with catch @ 00b4fff0 */
                          if (DAT_01126840 == 0) {
                    /* catch() { ... } // from try @ 00b4adb4 with catch @ 00b4fff4 */
                    /* catch() { ... } // from try @ 00b49424 with catch @ 00b50004 */
                    /* catch() { ... } // from try @ 00b4fa50 with catch @ 00b50008
                       catch() { ... } // from try @ 00b4fb88 with catch @ 00b50008 */
                    /* catch() { ... } // from try @ 00b49d9c with catch @ 00b5000c */
                            DAT_01126840 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                     (param_1,param_2,0,
                                                      "dalvik/system/DexClassLoader",0);
                          }
                          uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                            (param_1,DAT_01126840,&PTR_s_<init>_00c909d8,2,
                                             &DAT_01126850,"dalvik/system/DexClassLoader");
                          if ((uVar8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b49d2c with catch @ 00b50040 */
                            if (DAT_01126b00 == 0) {
                              DAT_01126b00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                       (param_1,param_2,0,"java/lang/Double",0);
                            }
                    /* catch() { ... } // from try @ 00b49cbc with catch @ 00b50074 */
                    /* catch() { ... } // from try @ 00b4bedc with catch @ 00b5008c */
                            uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                              (param_1,DAT_01126b00,&PTR_s_<init>_00c90e28,2,
                                               &DAT_01126b10,"java/lang/Double");
                            if ((uVar8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4ac8c with catch @ 00b500a0 */
                    /* catch() { ... } // from try @ 00b49b2c with catch @ 00b500a4 */
                    /* catch() { ... } // from try @ 00b498f4 with catch @ 00b500a8 */
                              if (DAT_01126b28 == 0) {
                    /* catch() { ... } // from try @ 00b4ab60 with catch @ 00b500ac */
                    /* catch() { ... } // from try @ 00b4a8dc with catch @ 00b500c4
                       catch() { ... } // from try @ 00b4aaec with catch @ 00b500c4 */
                                DAT_01126b28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                         (param_1,param_2,0,"java/lang/Enum",0);
                    /* catch() { ... } // from try @ 00b493f0 with catch @ 00b500c8 */
                    /* catch() { ... } // from try @ 00b4f71c with catch @ 00b500cc */
                              }
                    /* catch() { ... } // from try @ 00b4a088 with catch @ 00b500d4 */
                    /* catch() { ... } // from try @ 00b4f854 with catch @ 00b500dc */
                              uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                (param_1,DAT_01126b28,&PTR_s_equals_00c90e58,2,
                                                 &DAT_01126b38,"java/lang/Enum");
                              if ((uVar8 & 1) != 0) {
                                if (DAT_01126b50 == 0) {
                    /* catch() { ... } // from try @ 00b4a1bc with catch @ 00b5011c */
                                  DAT_01126b50 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                           (param_1,param_2,0,"java/io/File",0);
                                }
                                uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                  (param_1,DAT_01126b50,&PTR_s_<init>_00c90e88,8,
                                                   &DAT_01126b60,"java/io/File");
                                if ((uVar8 & 1) != 0) {
                                  if (DAT_01126810 == 0) {
                    /* catch() { ... } // from try @ 00b4f684 with catch @ 00b50170 */
                    /* catch() { ... } // from try @ 00b4aa00 with catch @ 00b50174 */
                                    DAT_01126810 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,
                                                             "java/io/FileOutputStream",0);
                                  }
                    /* catch() { ... } // from try @ 00b4a020 with catch @ 00b50188 */
                                  uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                    (param_1,DAT_01126810,&PTR_s_<init>_00c90990,3,
                                                     &DAT_01126820,"java/io/FileOutputStream");
                    /* catch() { ... } // from try @ 00b4d778 with catch @ 00b501ac */
                    /* catch() { ... } // from try @ 00b4d4fc with catch @ 00b501b0 */
                                  if ((uVar8 & 1) != 0) {
                                    if (DAT_01126ba8 == 0) {
                    /* catch() { ... } // from try @ 00b49918 with catch @ 00b501c4 */
                    /* catch() { ... } // from try @ 00b4d7b8 with catch @ 00b501d4 */
                    /* catch() { ... } // from try @ 00b4d53c with catch @ 00b501d8 */
                                      DAT_01126ba8 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Float",0);
                                    }
                                    uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                      (param_1,DAT_01126ba8,&PTR_s_<init>_00c90f48,2
                                                       ,&DAT_01126bb8,"java/lang/Float");
                                    if ((uVar8 & 1) != 0) {
                    /* try { // try from 00b50210 to 00c502ef has its CatchHandler @ 00b50210
                       catch() { ... } // from try @ 00b50210 with catch @ 00b50210
                       catch() { ... } // from try @ 00b502f8 with catch @ 00b50210
                       catch() { ... } // from try @ 00b50340 with catch @ 00b50210 */
                                      if (DAT_01126bd0 == 0) {
                                        DAT_01126bd0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/util/HashMap",0
                                                            );
                                      }
                                      uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                        (param_1,DAT_01126bd0,&PTR_s_<init>_00c90f78
                                                         ,1,&DAT_01126be0,"java/util/HashMap");
                                      if ((uVar8 & 1) != 0) {
                                        if (DAT_01126bf0 == 0) {
                                          DAT_01126bf0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Integer",0
                                                            );
                                        }
                                        uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                          (param_1,DAT_01126bf0,
                                                           &PTR_s_<init>_00c90f90,2,&DAT_01126c00,
                                                           "java/lang/Integer");
                                        if ((uVar8 & 1) != 0) {
                                          if (DAT_01126c18 == 0) {
                                            DAT_01126c18 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,
                                                             "android/content/Intent",0);
                    /* try { // try from 00b502f0 to 00c502f7 has its CatchHandler @ 00b50340 */
                                          }
                    /* try { // try from 00b502f8 to 00c50337 has its CatchHandler @ 00b50210 */
                                          uVar8 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126c18,
                                                             &PTR_s_<init>_00c90fc0,5,&DAT_01126c28,
                                                             "android/content/Intent");
                                          if ((uVar8 & 1) != 0) {
                                            if (DAT_01126c58 == 0) {
                    /* try { // try from 00b50338 to 00c5033f has its CatchHandler @ 00b50340 */
                    /* catch() { ... } // from try @ 00b502f0 with catch @ 00b50340
                       catch() { ... } // from try @ 00b50338 with catch @ 00b50340
                       try { // try from 00b50340 to 00c5035b has its CatchHandler @ 00b50210 */
                                              DAT_01126c58 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Iterable",
                                                             0);
                                            }
                                            uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126c58,
                                                             &PTR_s_iterator_00c91038,1,
                                                             &DAT_01126c68,"java/lang/Iterable");
                                            if ((uVar8 & 1) != 0) {
                                              if (DAT_01126c78 == 0) {
                                                DAT_01126c78 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/util/Iterator",
                                                             0);
                                              }
                                              uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126c78,
                                                             &PTR_s_hasNext_00c91050,2,&DAT_01126c88
                                                             ,"java/util/Iterator");
                                              if ((uVar8 & 1) != 0) {
                                                if (DAT_01126ca0 == 0) {
                                                  DAT_01126ca0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/util/List",0);
                                                }
                    /* try { // try from 00b50418 to 00c5125b has its CatchHandler @ 00b50418
                       catch() { ... } // from try @ 00b50418 with catch @ 00b50418
                       catch() { ... } // from try @ 00b51280 with catch @ 00b50418
                       catch() { ... } // from try @ 00b512f4 with catch @ 00b50418 */
                                                uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126ca0,&PTR_DAT_00c91080,
                                                             3,&DAT_01126cb0,"java/util/List");
                                                if ((uVar8 & 1) != 0) {
                                                  if (DAT_01126cd0 == 0) {
                                                    DAT_01126cd0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Long",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126cd0,
                                                             &PTR_s_<init>_00c910c8,2,&DAT_01126ce0,
                                                             "java/lang/Long");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126cf8 == 0) {
                                                      DAT_01126cf8 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/util/Map",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126cf8,&PTR_DAT_00c910f8,
                                                             3,&DAT_01126d08,"java/util/Map");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126d28 == 0) {
                                                      DAT_01126d28 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,
                                                             "android/os/ParcelFileDescriptor",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126d28,
                                                             &PTR_s_detachFd_00c91140,1,
                                                             &DAT_01126d38,
                                                             "android/os/ParcelFileDescriptor");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126868 == 0) {
                                                      DAT_01126868 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,
                                                             "android/content/res/Resources",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126868,
                                                             &PTR_s_getIdentifier_00c90a08,1,
                                                             &DAT_01126878,
                                                             "android/content/res/Resources");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126d48 == 0) {
                                                      DAT_01126d48 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/util/Set",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126d48,
                                                             &PTR_s_iterator_00c91158,1,
                                                             &DAT_01126d58,"java/util/Set");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126d68 == 0) {
                                                      DAT_01126d68 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Short",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126d68,
                                                             &PTR_s_<init>_00c91170,2,&DAT_01126d78,
                                                             "java/lang/Short");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126d90 == 0) {
                                                      DAT_01126d90 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/String",0)
                                                  ;
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126d90,
                                                             &PTR_s_<init>_00c911a0,1,&DAT_01126da0,
                                                             "java/lang/String");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126db0 == 0) {
                                                      DAT_01126db0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Throwable"
                                                             ,0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126db0,
                                                             &PTR_s_getLocalizedMessage_00c911b8,3,
                                                             &DAT_01126dc0,"java/lang/Throwable");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126de0 == 0) {
                                                      DAT_01126de0 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"android/net/Uri",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126de0,
                                                             &PTR_s_toString_00c91200,2,
                                                             &DAT_01126df0,"android/net/Uri");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_01126e08 == 0) {
                                                      DAT_01126e08 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/lang/Object",0)
                                                  ;
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126e08,
                                                             &PTR_s_toString_00c91230,1,
                                                             &DAT_01126e18,"java/lang/Object");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_011267b8 == 0) {
                                                      DAT_011267b8 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,
                                                             "android/net/Uri$Builder",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_011267b8,
                                                             &PTR_s_<init>_00c90918,3,&DAT_011267c8,
                                                             "android/net/Uri$Builder");
                                                  if ((uVar8 & 1) != 0) {
                                                    if (DAT_011267e8 == 0) {
                                                      DAT_011267e8 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,0,"java/net/URL",0);
                                                  }
                                                  uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_011267e8,
                                                             &PTR_s_<init>_00c90960,2,&DAT_011267f8,
                                                             "java/net/URL");
                                                  if ((uVar8 & 1) != 0) {
                                                    DAT_01126e38 = DAT_01126e38 + 1;
                                                    uVar11 = *(undefined8 *)
                                                                                                                            
                                                  PTR__ZN12firebase_app18app_resources_sizeE_00c9c7c0
                                                  ;
                                                  local_88 = (undefined8 *)_Znwm(0x18);
                                                  puVar4 = 
                                                  PTR__ZN12firebase_app22app_resources_filenameE_00c9c7c8
                                                  ;
                                                  puVar3 = 
                                                  PTR__ZN12firebase_app18app_resources_dataE_00c9c7b8
                                                  ;
                                                  local_80 = local_88 + 3;
                                                  local_88[2] = uVar11;
                                                  local_88[1] = puVar3;
                                                  *local_88 = puVar4;
                                                  local_78 = local_80;
                                                  puVar9 = (undefined8 *)
                                                                                                                      
                                                  _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE
                                                            (param_1,param_2,&local_88);
                                                  __src = (undefined8 *)*puVar9;
                                                  local_68 = (void *)0x0;
                                                  pvStack_60 = (void *)0x0;
                                                  local_70 = (void *)0x0;
                                                  uVar8 = puVar9[1] - (long)__src;
                                                  if (uVar8 != 0) {
                                                    if (0xaaaaaaaaaaaaaaa <
                                                        (ulong)(((long)uVar8 >> 3) *
                                                               -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
                                                      abort();
                                                    }
                                                    __dest = (void *)_Znwm(uVar8);
                                                    pvStack_60 = (void *)((long)__dest +
                                                                         ((long)uVar8 >> 3) * 8);
                                                    local_70 = __dest;
                                                    local_68 = __dest;
                                                    if (0 < (long)uVar8) {
                                                      memcpy(__dest,__src,uVar8);
                                                      local_68 = (void *)((long)__dest +
                                                                         (uVar8 / 0x18) * 0x18);
                                                    }
                                                  }
                                                  if (__src != (undefined8 *)0x0) {
                                                    local_80 = __src;
                                                    _ZdlPv(__src);
                                                  }
                                                  if ((((DAT_01126798 == 0) &&
                                                       (DAT_01126798 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,&local_70,
                                                                                                                          
                                                  "com/google/firebase/app/internal/cpp/Log",0),
                                                  DAT_01126798 == 0)) ||
                                                  (uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126798,
                                                             &PTR_s_shutdown_00c90900,1,
                                                             &DAT_011267a8,
                                                                                                                          
                                                  "com/google/firebase/app/internal/cpp/Log"),
                                                  (uVar8 & 1) == 0)) || (DAT_011267a0 != '\0')) {
LAB_00b50c24:
                                                    uVar10 = 0;
                                                    pcVar2 = (code *)
                                                  PTR__ZN8firebase4util9TerminateEP7_JNIEnv_00c9c768
                                                  ;
                                                  }
                                                  else {
                                                    iVar7 = (**(code **)(*param_1 + 0x6b8))
                                                                      (param_1,DAT_01126798,
                                                                       &PTR_s_nativeLog_00c91248,1);
                                                    cVar6 = (**(code **)(*param_1 + 0x720))(param_1)
                                                    ;
                                                    if (cVar6 != '\0') {
                                                      (**(code **)(*param_1 + 0x80))(param_1);
                                                      (**(code **)(*param_1 + 0x88))(param_1);
                                                    }
                                                    DAT_011267a0 = iVar7 == 0;
                                                    if (iVar7 != 0) goto LAB_00b50c24;
                                                    if ((DAT_01126710 == 0) &&
                                                       (DAT_01126710 = 
                                                  _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                                            (param_1,param_2,&local_70,
                                                                                                                          
                                                  "com/google/firebase/app/internal/cpp/JniResultCallback"
                                                  ,0), DAT_01126710 == 0)) {
                                                    bVar5 = false;
                                                  }
                                                  else {
                                                    uVar8 = 
                                                  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                                                            (param_1,DAT_01126710,
                                                             &PTR_s_<init>_00c90840,2,&DAT_01126720,
                                                                                                                          
                                                  "com/google/firebase/app/internal/cpp/JniResultCallback"
                                                  );
                                                  bVar5 = false;
                                                  if (((uVar8 & 1) != 0) && (DAT_01126718 == '\0'))
                                                  {
                                                    iVar7 = (**(code **)(*param_1 + 0x6b8))
                                                                      (param_1,DAT_01126710,
                                                                       &
                                                  PTR_s_nativeOnResult_00c91260,1);
                                                  cVar6 = (**(code **)(*param_1 + 0x720))(param_1);
                                                  if (cVar6 != '\0') {
                                                    (**(code **)(*param_1 + 0x80))(param_1);
                                                    (**(code **)(*param_1 + 0x88))(param_1);
                                                  }
                                                  DAT_01126718 = iVar7 == 0;
                                                  bVar5 = (bool)DAT_01126718;
                                                  }
                                                  }
                                                  DAT_01126e3c = bVar5;
                                                  uVar8 = 
                                                  _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
                                                            (param_1,param_2,&local_70);
                                                  if ((uVar8 & 1) == 0) goto LAB_00b50c24;
                                                  cVar6 = (**(code **)(*param_1 + 0x720))(param_1);
                                                  if (cVar6 != '\0') {
                                                    (**(code **)(*param_1 + 0x80))(param_1);
                                                    (**(code **)(*param_1 + 0x88))(param_1);
                                                  }
                                                  DAT_01126e40 = (undefined8 *)_Znwm(0x18);
                                                  DAT_01126e40[1] = 0;
                                                  uVar10 = 1;
                                                  DAT_01126e40[2] = 0;
                                                  uRam0000000001126e50 = 0;
                                                  _DAT_01126e48 = 0;
                                                  uRam0000000001126e60 = 0;
                                                  _DAT_01126e58 = 0;
                                                  DAT_01126e68 = 0;
                                                  *DAT_01126e40 = DAT_01126e40 + 1;
                                                  pcVar2 = (code *)0x0;
                                                  }
                                                  if (local_70 != (void *)0x0) {
                                                    local_68 = local_70;
                                                    _ZdlPv(local_70);
                                                  }
                                                  if (pcVar2 != (code *)0x0) {
                                                    (*pcVar2)(param_1);
                                                  }
                                                  goto LAB_00b50b48;
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    FUN_00b50c50(param_1);
    _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv(param_1);
  }
  uVar10 = 0;
LAB_00b50b48:
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar10);
}

~~~
