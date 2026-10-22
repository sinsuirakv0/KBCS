# 00bce6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bce6ac.md)

## 関数情報

~~~json
{
  "address": "00bce6ac",
  "name": "FUN_00bce6ac",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6aca06a13a5afc572c89afcbe3c2b5e4f49417a7bf3a8238053382ddfcb74756",
  "source_text_sha256": "6aca06a13a5afc572c89afcbe3c2b5e4f49417a7bf3a8238053382ddfcb74756"
}
~~~
## 呼び出し元

- [00bc66f0](../00bc6/00bc66f0.md)
- [00bce830](../00bce/00bce830.md)

## 呼び出し先

- [00bc1bc0](../00bc1/00bc1bc0.md)
- [00bc1f84](../00bc1/00bc1f84.md)
- [00bc20b8](../00bc2/00bc20b8.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 2533 bytes

~~~c

void FUN_00bce6ac(long *param_1)

{
  char cVar1;
  long lVar2;
  long *__ptr;
  void *__dest;
  size_t __n;
  long *plVar3;
  long *plVar4;
  
  if ((char *)param_1[1] == (char *)*param_1) {
LAB_00bce730:
    FUN_00bc20b8();
    return;
  }
  cVar1 = *(char *)*param_1;
  if (cVar1 == 'D') {
    lVar2 = FUN_00bc1f84();
    if (lVar2 == 0) {
      return;
    }
    plVar4 = (long *)param_1[0x26];
    if (plVar4 != (long *)param_1[0x27]) goto LAB_00bce804;
    plVar3 = (long *)param_1[0x25];
    __n = (long)plVar4 - (long)plVar3;
    if (plVar3 == param_1 + 0x28) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (plVar4 != plVar3) {
        memmove(__dest,plVar3,__n);
      }
LAB_00bce7e8:
      param_1[0x25] = (long)__dest;
    }
    else {
      __dest = realloc(plVar3,__n * 2);
      param_1[0x25] = (long)__dest;
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
  }
  else {
    if (cVar1 != 'T') goto LAB_00bce730;
                    /* try { // try from 00bce6e8 to 00cce6f7 has its CatchHandler @ 00bcf2e0 */
    lVar2 = FUN_00bc1bc0();
    if (lVar2 == 0) {
      return;
    }
    plVar4 = (long *)param_1[0x26];
                    /* try { // try from 00bce6f8 to 00cce703 has its CatchHandler @ 00bcf2c0 */
    if (plVar4 != (long *)param_1[0x27]) goto LAB_00bce804;
    __ptr = (long *)param_1[0x25];
                    /* try { // try from 00bce708 to 00cce723 has its CatchHandler @ 00bcf274 */
    plVar3 = param_1 + 0x28;
    __n = (long)plVar4 - (long)__ptr;
    if (__ptr == plVar3) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (plVar4 != plVar3) {
        memcpy(__dest,plVar3,__n);
      }
      goto LAB_00bce7e8;
    }
    __dest = realloc(__ptr,__n * 2);
                    /* try { // try from 00bce724 to 00cce887 has its CatchHandler @ 00bce4cc */
    param_1[0x25] = (long)__dest;
    if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
  }
  plVar4 = (long *)((long)__dest + __n);
  param_1[0x27] = (long)((long)__dest + ((long)__n >> 2) * 8);
LAB_00bce804:
  param_1[0x26] = (long)(plVar4 + 1);
  *plVar4 = lVar2;
  return;
}

~~~
