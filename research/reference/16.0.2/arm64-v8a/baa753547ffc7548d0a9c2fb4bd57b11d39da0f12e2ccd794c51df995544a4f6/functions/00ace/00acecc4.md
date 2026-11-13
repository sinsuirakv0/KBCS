# 00acecc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acecc4",
  "name": "FUN_00acecc4",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538",
  "source_text_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538"
}
~~~

## 呼び出し元

- [0066242c](../00662/0066242c.md)
- [006624d0](../00662/006624d0.md)
- [00662574](../00662/00662574.md)
- [007ccf44](../007cc/007ccf44.md)
- [007de918](../007de/007de918.md)
- [008c42e4](../008c4/008c42e4.md)
- [00a47f54](../00a47/00a47f54.md)
- [00acc640](../00acc/00acc640.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)
- [00ad09c8](../00ad0/00ad09c8.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00802710](../00802/00802710.md)
- [00aeae8c](../00aea/00aeae8c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 2554 bytes

~~~c

uint FUN_00acecc4(long param_1,int param_2)

{
  void *__src;
  void *pvVar1;
  size_t __n;
  long lVar2;
  long *plVar3;
  bool bVar4;
  int iVar5;
  uint uVar6;
  void *__dest;
  size_t sVar7;
  long *plVar8;
  long *plVar9;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
                    /* try { // try from 00acecd8 to 00bcece3 has its CatchHandler @ 00acf64c */
                    /* try { // try from 00acece4 to 00bced03 has its CatchHandler @ 00acf5f8 */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar5 = FUN_00802710(0);
                    /* try { // try from 00aced04 to 00bcee53 has its CatchHandler @ 00accbd0 */
  if ((0x13 < iVar5 + 0x19U) || ((0x87c01U >> (ulong)(iVar5 + 0x19U & 0x1f) & 1) == 0)) {
    plVar8 = *(long **)(param_1 + 0x33c0);
    while (plVar8 != (long *)(param_1 + 0x33c8)) {
      __src = (void *)plVar8[5];
      pvVar1 = (void *)plVar8[6];
      local_78 = 0;
      uStack_70 = 0;
      __n = (long)pvVar1 - (long)__src;
      local_80 = 0;
      if (__n != 0) {
        if ((long)__n < 0) {
          if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00acee54 to 00bcee6f has its CatchHandler @ 00acf5e4 */
                    /* WARNING: Subroutine does not return */
            FUN_00470880(&local_80);
          }
          goto LAB_00acee8c;
        }
        __dest = (void *)_Znwm(__n);
        memcpy(__dest,__src,__n);
        if (pvVar1 != __src) {
          sVar7 = 0;
          do {
            if (*(int *)((long)__dest + sVar7) == param_2) {
              _ZdlPv(__dest);
              uVar6 = 1;
              goto LAB_00acee14;
            }
            sVar7 = sVar7 + 4;
          } while (__n != sVar7);
        }
        _ZdlPv(__dest);
      }
      plVar3 = (long *)plVar8[1];
      plVar9 = plVar8;
      if ((long *)plVar8[1] == (long *)0x0) {
        do {
          plVar8 = (long *)plVar9[2];
          bVar4 = (long *)*plVar8 != plVar9;
          plVar9 = plVar8;
        } while (bVar4);
      }
      else {
        do {
          plVar8 = plVar3;
          plVar3 = (long *)*plVar8;
        } while ((long *)*plVar8 != (long *)0x0);
      }
    }
    if (999999999 < param_2) {
      uVar6 = FUN_00aeae8c(param_1,param_2);
      uVar6 = ~uVar6 >> 0x1f;
      goto LAB_00acee14;
    }
  }
  uVar6 = 0;
LAB_00acee14:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar6;
  }
LAB_00acee8c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
