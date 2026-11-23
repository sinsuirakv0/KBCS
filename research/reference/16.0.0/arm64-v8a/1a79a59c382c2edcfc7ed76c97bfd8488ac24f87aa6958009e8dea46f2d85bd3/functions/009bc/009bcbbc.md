# 009bcbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009870dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md) · 移動量 `+0x35ae0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0012.md#compare-4f7ad2c0040e14315edc5d459c667638)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009bcbbc",
  "name": "FUN_009bcbbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3",
  "source_text_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3"
}
~~~

## 呼び出し元

- [009bd99c](../009bd/009bd99c.md)
- [009bdae4](../009bd/009bdae4.md)

## 呼び出し先

- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)

## 疑似コード / UTF-8 1708 bytes

~~~c

void FUN_009bcbbc(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[1];
                    /* try { // try from 009bcbd0 to 00abcccb has its CatchHandler @ 009bc884 */
  *param_1 = 0;
  param_1[1] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[3];
  param_1[2] = 0;
  param_1[3] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[5];
  param_1[4] = 0;
  param_1[5] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[7];
  param_1[6] = 0;
  param_1[7] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[9];
  param_1[8] = 0;
  param_1[9] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* try { // try from 009bcccc to 00abcce3 has its CatchHandler @ 009bda34 */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~
