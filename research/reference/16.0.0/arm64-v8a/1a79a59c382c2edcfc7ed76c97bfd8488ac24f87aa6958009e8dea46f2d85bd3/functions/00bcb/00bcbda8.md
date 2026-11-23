# 00bcbda8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c8a8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0066.md#compare-0d85c0f4fbec391f3eafde2f97d0ee7e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbda8",
  "name": "_ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae",
  "source_text_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae"
}
~~~

## 呼び出し元

- [00c5d5a0](../00c5d/00c5d5a0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 823 bytes

~~~c

void _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE(long param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  ulong uVar4;
  
  plVar2 = *(long **)(param_1 + 0x220);
  plVar3 = *(long **)(param_1 + 0x218);
  if (plVar2 != plVar3) {
    uVar4 = 0;
    plVar1 = (long *)*plVar3;
    plVar2 = plVar3;
    while( true ) {
      if (plVar1 != (long *)0x0) {
        (**(code **)(*plVar1 + 8))();
        plVar2 = *(long **)(param_1 + 0x218);
      }
      plVar2[uVar4] = 0;
      plVar2 = *(long **)(param_1 + 0x218);
      uVar4 = uVar4 + 1;
      if ((ulong)(*(long *)(param_1 + 0x220) - (long)plVar2 >> 3) <= uVar4) break;
                    /* catch() { ... } // from try @ 00bcbd90 with catch @ 00bcbdf4 */
      plVar1 = (long *)plVar2[uVar4];
    }
  }
  *(long **)(param_1 + 0x220) = plVar2;
  return;
}

~~~
