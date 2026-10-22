# 00afacd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afacd8.md)

## 関数情報

~~~json
{
  "address": "00afacd8",
  "name": "std::__ndk1::vector<firebase::App*,std::__ndk1::allocator<firebase::App*>>::__push_back_slow_path<firebase::App*const&>",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3bd059109f97747a35329612de8e4e27ff9bbba543e2d83dd3af8a84156d9031",
  "source_text_sha256": "3bd059109f97747a35329612de8e4e27ff9bbba543e2d83dd3af8a84156d9031"
}
~~~
## 呼び出し元

- [00bde8c0](../00bde/00bde8c0.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 2044 bytes

~~~c

/* void std::__ndk1::vector<firebase::App*, std::__ndk1::allocator<firebase::App*>
   >::__push_back_slow_path<firebase::App* const&>(firebase::App* const&) */

void __thiscall
std::__ndk1::vector<firebase::App*,std::__ndk1::allocator<firebase::App*>>::
__push_back_slow_path<firebase::App*const&>
          (vector<firebase::App*,std::__ndk1::allocator<firebase::App*>> *this,App **param_1)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
  __src = *(void **)this;
  __n = *(long *)(this + 8) - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afad3c:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afad10 to 00bfad23 has its CatchHandler @ 00aff510 */
  if ((ulong)(*(long *)(this + 0x10) - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = *(long *)(this + 0x10) - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afad50;
    }
                    /* try { // try from 00afad34 to 00bfad3b has its CatchHandler @ 00aff50c */
    if (uVar3 >> 0x3d != 0) goto LAB_00afad3c;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = operator_new(uVar3 << 3);
LAB_00afad50:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_1;
                    /* try { // try from 00afad64 to 00bfad77 has its CatchHandler @ 00aff508 */
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *(void **)this = __dest;
  *(undefined8 **)(this + 8) = puVar1 + 1;
  *(void **)(this + 0x10) = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afad88 to 00bfadab has its CatchHandler @ 00b0037c */
    operator_delete(__src);
    return;
  }
                    /* try { // try from 00afadac to 00bfadb3 has its CatchHandler @ 00aff504 */
  return;
}

~~~
