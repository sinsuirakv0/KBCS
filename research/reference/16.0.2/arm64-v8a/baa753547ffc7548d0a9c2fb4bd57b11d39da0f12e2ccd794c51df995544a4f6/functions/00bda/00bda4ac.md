# 00bda4ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bda4ac",
  "name": "_ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e684b7a814888622a7641a9c9a1b9bcb7be0717675f8ce2c05cd72087a8df0e4",
  "source_text_sha256": "e684b7a814888622a7641a9c9a1b9bcb7be0717675f8ce2c05cd72087a8df0e4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5dc20](../00c5d/00c5dc20.md)
- [00c5dea0](../00c5d/00c5dea0.md)
- [00c5df20](../00c5d/00c5df20.md)

## 関連文字列（未確認候補）

~~~text
"GameCenter is not supported on Android."
"is_gamecenter_available_on_android"
~~~

## 疑似コード / UTF-8 1888 bytes

~~~c

void _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv(undefined8 param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  undefined1 auStack_68 [16];
  undefined1 auStack_58 [16];
  undefined1 auStack_48 [16];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZN8firebase4auth23GetCredentialFutureImplEv();
  puVar3 = (undefined8 *)_Znwm(0x28);
  *puVar3 = 0;
  *(undefined4 *)(puVar3 + 1) = 0;
  puVar3[3] = 0;
  puVar3[4] = 0;
  puVar3[2] = 0;
                    /* try { // try from 00bda4f0 to 00cda4fb has its CatchHandler @ 00bdef30 */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_48,uVar2,0,puVar3,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv_00c9bb00
            );
                    /* try { // try from 00bda510 to 00cda52f has its CatchHandler @ 00bdeef8 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_58,auStack_48);
  _ZN8firebase12FutureHandleD2Ev(auStack_48);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,auStack_58);
                    /* try { // try from 00bda530 to 00cdb763 has its CatchHandler @ 00bd6fbc */
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
            (uVar2,auStack_68,4,"GameCenter is not supported on Android.",auStack_48);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase9LogAssertEPKcz("is_gamecenter_available_on_android");
  _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar2,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
