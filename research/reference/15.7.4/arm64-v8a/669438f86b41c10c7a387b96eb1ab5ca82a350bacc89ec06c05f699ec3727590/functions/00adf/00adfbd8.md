# 00adfbd8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00adfacc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfacc.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00adfbd8",
  "name": "FUN_00adfbd8",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "662259eb59ac85ac81f17aa66a9e7cb5b0bd6f7d879e66916afab1a81167fa63",
  "source_text_sha256": "662259eb59ac85ac81f17aa66a9e7cb5b0bd6f7d879e66916afab1a81167fa63"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00444c54](../00444/00444c54.md)
- [0044592c](../00445/0044592c.md)
- [00467c58](../00467/00467c58.md)
- [00886014](../00886/00886014.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

## 疑似コード / UTF-8 4120 bytes

~~~c

void FUN_00adfbd8(undefined8 param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int extraout_var;
  int extraout_w1;
  int extraout_var_00;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00adfbec to 00bdfbef has its CatchHandler @ 00adfc44 */
  uVar4 = *param_3;
  uVar5 = *param_2;
                    /* try { // try from 00adfc04 to 00bdfc23 has its CatchHandler @ 00adfc40 */
  FUN_00444c54(uVar4,0xbe,0xbe,0xbe,0xff);
                    /* catch() { ... } // from try @ 00adf228 with catch @ 00adfc24
                       catch() { ... } // from try @ 00adf338 with catch @ 00adfc24
                       catch() { ... } // from try @ 00adf434 with catch @ 00adfc24
                       try { // try from 00adfc24 to 00bdfd23 has its CatchHandler @ 00adec50 */
                    /* catch() { ... } // from try @ 00adfbd0 with catch @ 00adfc28 */
                    /* catch() { ... } // from try @ 00adf074 with catch @ 00adfc2c */
                    /* catch() { ... } // from try @ 00adf070 with catch @ 00adfc30 */
                    /* catch() { ... } // from try @ 00adf020 with catch @ 00adfc34 */
  lVar3 = __dynamic_cast(DAT_00c24ab8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8e98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8ea8,0);
                    /* catch() { ... } // from try @ 00adef60 with catch @ 00adfc38 */
  uVar6 = *(undefined8 *)(lVar3 + 0x38);
                    /* catch() { ... } // from try @ 00adef9c with catch @ 00adfc3c
                       catch() { ... } // from try @ 00adf27c with catch @ 00adfc3c */
                    /* catch() { ... } // from try @ 00adfb98 with catch @ 00adfc40
                       catch() { ... } // from try @ 00adfc04 with catch @ 00adfc40 */
  iVar1 = FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfb7c with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfbb4 with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfbec with catch @ 00adfc44 */
                    /* catch() { ... } // from try @ 00adf10c with catch @ 00adfc48 */
                    /* catch() { ... } // from try @ 00adf600 with catch @ 00adfc4c */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfaf8 with catch @ 00adfc50
                       catch() { ... } // from try @ 00adfb30 with catch @ 00adfc50 */
                    /* catch() { ... } // from try @ 00adee60 with catch @ 00adfc54 */
                    /* catch() { ... } // from try @ 00adecc4 with catch @ 00adfc58
                       catch() { ... } // from try @ 00adfadc with catch @ 00adfc58 */
  lVar3 = __dynamic_cast(DAT_00c24ab8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8e98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8ea8,0);
  iVar2 = FUN_00467c58(*(undefined8 *)(lVar3 + 0x38));
                    /* catch() { ... } // from try @ 00adfac4 with catch @ 00adfc74
                       catch() { ... } // from try @ 00adfb14 with catch @ 00adfc74
                       catch() { ... } // from try @ 00adfb64 with catch @ 00adfc74 */
                    /* catch() { ... } // from try @ 00adedb8 with catch @ 00adfc78 */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfa90 with catch @ 00adfc7c */
  FUN_00886014(uVar5);
                    /* catch() { ... } // from try @ 00adfa74 with catch @ 00adfc88
                       catch() { ... } // from try @ 00adfaac with catch @ 00adfc88 */
                    /* catch() { ... } // from try @ 00adfa40 with catch @ 00adfc9c */
                    /* catch() { ... } // from try @ 00adf8a0 with catch @ 00adfca0 */
                    /* catch() { ... } // from try @ 00adf850 with catch @ 00adfca4
                       catch() { ... } // from try @ 00adf8d8 with catch @ 00adfca4 */
  FUN_0044592c(uVar4,uVar6,(extraout_w1 + iVar1) - iVar2,extraout_var_00 + extraout_var,0);
  return;
}

~~~
