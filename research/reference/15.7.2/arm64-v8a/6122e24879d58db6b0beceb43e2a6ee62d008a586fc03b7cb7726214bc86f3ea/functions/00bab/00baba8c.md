# 00baba8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00babb98`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babb98.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baba8c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ab322ba6d65757ed0cb93138ab7d0fea5f9e18099ea862b68ff74af9d56fe00",
  "source_text_sha256": "9ab322ba6d65757ed0cb93138ab7d0fea5f9e18099ea862b68ff74af9d56fe00"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a80](../00be1/00be1a80.md)
- [00be1a90](../00be1/00be1a90.md)

## 疑似コード / UTF-8 698 bytes

~~~c

ulong _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv(long param_1)

{
  int iVar1;
  __locale_t p_Var2;
  ulong uVar3;
  size_t sVar4;
  
  p_Var2 = uselocale(*(__locale_t *)(param_1 + 0x10));
  iVar1 = mbtowc((wchar_t *)0x0,(char *)0x0,4);
  if (p_Var2 != (__locale_t)0x0) {
    uselocale(p_Var2);
  }
  if (iVar1 == 0) {
    if (*(__locale_t *)(param_1 + 0x10) == (__locale_t)0x0) {
      uVar3 = 1;
    }
    else {
      p_Var2 = uselocale(*(__locale_t *)(param_1 + 0x10));
      sVar4 = __ctype_get_mb_cur_max();
      if (p_Var2 != (__locale_t)0x0) {
        uselocale(p_Var2);
      }
      uVar3 = (ulong)(sVar4 == 1);
    }
  }
  else {
    uVar3 = 0xffffffff;
  }
  return uVar3;
}

~~~
