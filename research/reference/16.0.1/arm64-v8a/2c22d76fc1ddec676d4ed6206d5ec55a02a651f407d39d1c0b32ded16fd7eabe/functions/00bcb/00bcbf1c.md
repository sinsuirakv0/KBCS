# 00bcbf1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcbaf4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0081.md#compare-c141c6bcdaeecfd9ce6be8b2429f3873)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0090.md#compare-0fcdcdad20e8d5a7e94bb2b851b78e21)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbf1c",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39950dce15118708e420e0078208e3175d11eb2f52a8be1261591039a8e98e83",
  "source_text_sha256": "39950dce15118708e420e0078208e3175d11eb2f52a8be1261591039a8e98e83"
}
~~~

## 呼び出し元

- [00c5db10](../00c5d/00c5db10.md)

## 呼び出し先

- [00b402c0](../00b40/00b402c0.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5ad10](../00c5a/00c5ad10.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

## 疑似コード / UTF-8 1935 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
                    /* try { // try from 00bcbf2c to 00ccbf8b has its CatchHandler @ 00bcbf2c
                       catch() { ... } // from try @ 00bcbf2c with catch @ 00bcbf2c
                       catch() { ... } // from try @ 00bcbf98 with catch @ 00bcbf2c */
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcbf9c;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b402c0("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
                    /* try { // try from 00bcbf8c to 00ccbf97 has its CatchHandler @ 00bcbff0 */
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
                    /* try { // try from 00bcbf98 to 00ccc017 has its CatchHandler @ 00bcbf2c */
LAB_00bcbf9c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
    _ZdlPv(__src);
    return;
  }
                    /* catch() { ... } // from try @ 00bcbf8c with catch @ 00bcbff0 */
  return;
}

~~~
