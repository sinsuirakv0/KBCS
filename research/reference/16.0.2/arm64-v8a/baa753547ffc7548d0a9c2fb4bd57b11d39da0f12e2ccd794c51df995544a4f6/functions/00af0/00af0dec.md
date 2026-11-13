# 00af0dec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af0dec",
  "name": "FUN_00af0dec",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "abe2b46d1199256358f9ff65a5b13a0a8db7a5daf7aa25c4e270580195b55ae4",
  "source_text_sha256": "abe2b46d1199256358f9ff65a5b13a0a8db7a5daf7aa25c4e270580195b55ae4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00468ca0](../00468/00468ca0.md)
- [00469c44](../00469/00469c44.md)
- [0046d9b4](../0046d/0046d9b4.md)
- [00aea7c0](../00aea/00aea7c0.md)
- [00c586e0](../00c58/00c586e0.md)

## 疑似コード / UTF-8 1243 bytes

~~~c

void FUN_00af0dec(long param_1,undefined8 param_2,undefined8 *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  float fVar5;
  
  lVar4 = *(long *)(param_1 + 8);
  uVar3 = *param_3;
  if (DAT_00ca4a78 == 0) {
    lVar2 = 0;
  }
  else {
                    /* try { // try from 00af0e34 to 00bf0e3b has its CatchHandler @ 00af1018 */
    lVar2 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
  }
  FUN_00aea7c0(lVar4,0);
  FUN_00468ca0(uVar3,5);
  iVar1 = *(int *)((long)&fde_table_entry_00333a38.initial_loc + lVar4);
                    /* try { // try from 00af0e74 to 00bf0e87 has its CatchHandler @ 00af1010 */
  fVar5 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00336f60.initial_loc + lVar4)
                                     * 0x1e));
                    /* try { // try from 00af0e98 to 00bf0e9f has its CatchHandler @ 00af1020 */
  FUN_00469c44(uVar3,*(undefined8 *)(lVar2 + 0x2d0),(int)((float)(iVar1 + 0x82) + fVar5 * 10.0),
               *(int *)((long)&fde_table_entry_00333a38.data_loc + lVar4) + -6,0x60,0x60,0);
  FUN_00468ca0(uVar3,0);
  return;
}

~~~
