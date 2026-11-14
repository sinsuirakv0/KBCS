# 00bccfac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bccfac",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5cb2969490938d6531d05e92d364eeb10000ab02afe3702566f54ef965b2e771",
  "source_text_sha256": "5cb2969490938d6531d05e92d364eeb10000ab02afe3702566f54ef965b2e771"
}
~~~

## 呼び出し元

- [00c5ebb0](../00c5e/00c5ebb0.md)

## 呼び出し先

- [00b41350](../00b41/00b41350.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

## 疑似コード / UTF-8 1670 bytes

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
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
                    /* try { // try from 00bccff0 to 00cccffb has its CatchHandler @ 00bcd054 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
                    /* try { // try from 00bccffc to 00ccd07b has its CatchHandler @ 00bccf90 */
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcd02c;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b41350("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcd02c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
                    /* catch() { ... } // from try @ 00bccff0 with catch @ 00bcd054 */
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
    _ZdlPv(__src);
    return;
  }
  return;
}

~~~
