# 005cdabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0109.md#review-625ad47ee3cde854a98bf7ead5bde8b8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdabc",
  "name": "FUN_005cdabc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc27038fac49334efed3d06d0cc62f5911390438dc1766f3b4faf70c5af65b93",
  "source_text_sha256": "cc27038fac49334efed3d06d0cc62f5911390438dc1766f3b4faf70c5af65b93"
}
~~~

## 呼び出し元

- [005cd620](../005cd/005cd620.md)

## 呼び出し先

- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c5a3b0](../00c5a/00c5a3b0.md)

## 疑似コード / UTF-8 357 bytes

~~~c

void FUN_005cdabc(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9afb0,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9afb8);
}

~~~
