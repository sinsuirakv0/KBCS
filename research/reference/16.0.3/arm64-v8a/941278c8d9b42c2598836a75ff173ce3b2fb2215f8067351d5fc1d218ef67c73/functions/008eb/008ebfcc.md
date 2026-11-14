# 008ebfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "008ebfcc",
  "name": "FUN_008ebfcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7391e77aaa9f66185cf3ccc2b9b4ea694752e7e24787a2703f6749bc776d8ffa",
  "source_text_sha256": "7391e77aaa9f66185cf3ccc2b9b4ea694752e7e24787a2703f6749bc776d8ffa"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [004692e8](../00469/004692e8.md)
- [00469f64](../00469/00469f64.md)
- [008524fc](../00852/008524fc.md)
- [008ba294](../008ba/008ba294.md)
- [008ba29c](../008ba/008ba29c.md)
- [00a83b64](../00a83/00a83b64.md)
- [00a845ec](../00a84/00a845ec.md)
- [00c596b0](../00c59/00c596b0.md)

## 疑似コード / UTF-8 1575 bytes

~~~c

void FUN_008ebfcc(long param_1,undefined8 *param_2)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  undefined8 uVar5;
  long lVar6;
  int iVar7;
  
  uVar5 = *param_2;
  lVar6 = *(long *)(param_1 + 8);
  iVar1 = FUN_008ba294(uVar5);
  if (iVar1 != 0) {
    uVar5 = FUN_008ba29c(uVar5);
                    /* try { // try from 008ebff8 to 009ec007 has its CatchHandler @ 008f00a8 */
    if (DAT_00ca5a38 == 0) {
      lVar2 = 0;
    }
    else {
                    /* try { // try from 008ec008 to 009ec06b has its CatchHandler @ 008e00a4 */
      lVar2 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c748b0,0);
    }
    uVar3 = FUN_00467bc0();
    iVar4 = (int)uVar5;
    iVar7 = (int)((ulong)uVar5 >> 0x20);
    FUN_004692e8(uVar3,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xb9,iVar7 + -0x34,0);
    uVar5 = FUN_00467bc0();
                    /* try { // try from 008ec06c to 009ec07b has its CatchHandler @ 008f00a8 */
                    /* try { // try from 008ec07c to 009ec0d3 has its CatchHandler @ 008e00a4 */
    FUN_00469f64(uVar5,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xca,iVar7 + 0x2a,0x120,0x57,
                 *(int *)(lVar6 + 0x2c0) + 4);
    lVar6 = FUN_008524fc();
    iVar1 = FUN_00a83b64(lVar6 + 0x3078,0xd);
    lVar6 = FUN_008524fc();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
    FUN_00a845ec(0x3f800000,lVar6 + 0x3078,0xd,(iVar4 - (iVar1 >> 1)) + 0x159,iVar7 + 0x96,0);
    return;
  }
  return;
}

~~~
