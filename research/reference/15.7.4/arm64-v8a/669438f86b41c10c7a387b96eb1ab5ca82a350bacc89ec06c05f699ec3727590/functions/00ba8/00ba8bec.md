# 00ba8bec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00ba8ae0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ae0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00ba8bec",
  "name": "_ZNSt6__ndk114collate_bynameIcED1Ev",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fb404fda7b2729c94782a5773f6886e54c9755a72452fc37259e79afc567ef8",
  "source_text_sha256": "8fb404fda7b2729c94782a5773f6886e54c9755a72452fc37259e79afc567ef8"
}
~~~

## 呼び出し元

- [00be1940](../00be1/00be1940.md)

## 呼び出し先

- [00bdb4b0](../00bdb/00bdb4b0.md)
- [00be1930](../00be1/00be1930.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIcED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk114collate_bynameIcEE_00c1bf88 + 0x10);
                    /* try { // try from 00ba8c14 to 00ca8c1f has its CatchHandler @ 00ba8df4 */
  freelocale((__locale_t)param_1[2]);
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~
