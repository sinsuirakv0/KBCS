# 00a3cbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00a3cbf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cbf0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00a3cbac",
  "name": "FUN_00a3cbac",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5169c35275898f76d193e5948903f9b3febef997489273c4f2e3041e4e29f32",
  "source_text_sha256": "c5169c35275898f76d193e5948903f9b3febef997489273c4f2e3041e4e29f32"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0073ab94](../0073a/0073ab94.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 574 bytes

~~~c

void FUN_00a3cbac(void)

{
  long lVar1;
  long lVar2;
  byte local_40 [8];
  ulong local_38;
  void *pvStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_0081f580();
  FUN_0073ab94(local_40);
  if ((local_40[0] & 1) == 0) {
    local_38 = (ulong)(local_40[0] >> 1);
  }
  else {
    _ZdlPv(pvStack_30);
  }
  lVar2 = FUN_0081f580();
  *(bool *)(lVar2 + 0x4494ea) = local_38 == 0;
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
