# 00ba7ebc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00ba7db0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7db0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00ba7ebc",
  "name": "_ZNSt6__ndk16localeC1Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570",
  "source_text_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570"
}
~~~

## 呼び出し元

- [00bdd950](../00bdd/00bdd950.md)

## 呼び出し先

- [00bd6e60](../00bd6/00bd6e60.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)
- [00bdd980](../00bdd/00bdd980.md)
- [00be18d0](../00be1/00be18d0.md)

## 疑似コード / UTF-8 617 bytes

~~~c

void _ZNSt6__ndk16localeC1Ev(undefined8 *param_1)

{
  undefined *puVar1;
  bool bVar2;
  int iVar3;
  undefined8 uVar4;
  
  if (((DAT_010a2af0 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_010a2af0), iVar3 != 0)) {
    uVar4 = _ZNSt6__ndk16locale7classicEv();
    _ZNSt6__ndk16localeC1ERKS0_(&DAT_010a2ae8,uVar4);
    __cxa_guard_release(&DAT_010a2af0);
  }
  puVar1 = DAT_010a2ae8;
  bVar2 = DAT_010a2ae8 != &DAT_010a29a0;
                    /* try { // try from 00ba7ef4 to 00ca7eff has its CatchHandler @ 00ba8d5c */
  *param_1 = DAT_010a2ae8;
  if (bVar2) {
    FUN_00bd6e60(1,puVar1 + 8);
  }
  return;
}

~~~
