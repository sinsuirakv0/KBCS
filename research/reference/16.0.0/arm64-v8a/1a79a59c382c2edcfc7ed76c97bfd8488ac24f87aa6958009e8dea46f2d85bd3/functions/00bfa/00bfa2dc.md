# 00bfa2dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7d894`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-f2923b6e759a170f904614132c9b12a3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa2dc",
  "name": "_ZNSt6__ndk16thread4joinEv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487",
  "source_text_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487"
}
~~~

## 呼び出し元

- [00c57d70](../00c57/00c57d70.md)

## 呼び出し先

- [00c57d20](../00c57/00c57d20.md)
- [00c5d240](../00c5d/00c5d240.md)

## 関連文字列（未確認候補）

~~~text
"thread::join failed"
~~~

## 疑似コード / UTF-8 378 bytes

~~~c

void _ZNSt6__ndk16thread4joinEv(pthread_t *param_1)

{
  int iVar1;
  
  if (*param_1 == 0) {
    iVar1 = 0x16;
  }
  else {
    iVar1 = pthread_join(*param_1,(void **)0x0);
    if (iVar1 == 0) {
      *param_1 = 0;
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"thread::join failed");
}

~~~
