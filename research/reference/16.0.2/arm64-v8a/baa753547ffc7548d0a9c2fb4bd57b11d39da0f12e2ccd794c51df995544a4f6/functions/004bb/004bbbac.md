# 004bbbac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004bbb6c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0008.md#compare-955d90c2fe55c550376382be79e5f69b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0008.md#compare-fd5b2c1c3a60ab7d0bf09dc3b169ced8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "FUN_004bbbac",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac",
  "source_text_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac"
}
~~~

## 呼び出し元

- [004b6768](../004b6/004b6768.md)
- [004b993c](../004b9/004b993c.md)
- [004ba4d8](../004ba/004ba4d8.md)
- [004ddf48](../004dd/004ddf48.md)

## 呼び出し先

- [0043de18](../0043d/0043de18.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58740](../00c58/00c58740.md)

## 関連文字列（未確認候補）

~~~text
"bigint_divop divide by zero"
~~~

## 疑似コード / UTF-8 972 bytes

~~~c

ulong FUN_004bbbac(long param_1,ulong param_2,uint param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined1 auStack_50 [24];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if (param_3 == 0) {
    uVar3 = __cxa_allocate_exception(0x20);
    FUN_0043de18(auStack_50,"bigint_divop divide by zero");
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar3,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar3,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9ae00,FUN_005358a8);
    }
  }
  else if (*(long *)(lVar2 + 0x28) == local_38) {
    uVar1 = 0;
    if ((ulong)param_3 != 0) {
      uVar1 = (param_2 & 0xffffffff | param_1 << 0x20) / (ulong)param_3;
    }
    return uVar1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
