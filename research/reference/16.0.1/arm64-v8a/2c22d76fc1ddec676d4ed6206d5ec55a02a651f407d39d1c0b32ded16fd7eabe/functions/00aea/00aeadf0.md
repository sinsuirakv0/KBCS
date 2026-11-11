# 00aeadf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aeadf0",
  "name": "FUN_00aeadf0",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac52751192b8c558cac494945e4265f5dcc828c158cc1caf0bb077bebaa03f21",
  "source_text_sha256": "ac52751192b8c558cac494945e4265f5dcc828c158cc1caf0bb077bebaa03f21"
}
~~~

## 呼び出し元

- [00acec54](../00ace/00acec54.md)
- [00acee20](../00ace/00acee20.md)
- [00acf1b8](../00acf/00acf1b8.md)

## 呼び出し先

- [00470840](../00470/00470840.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)
- [00c58450](../00c58/00c58450.md)

## 疑似コード / UTF-8 4033 bytes

~~~c

int FUN_00aeadf0(long param_1,int param_2)

{
  void *__src;
  size_t __n;
  long lVar1;
  long *plVar2;
  bool bVar3;
  wchar_t *__s;
  wchar_t *pwVar4;
  int iVar5;
  wchar_t *pwVar6;
  long *plVar7;
  long *plVar8;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  plVar7 = *(long **)(param_1 + 0x33c0);
  if (plVar7 == (long *)(param_1 + 0x33c8)) {
    iVar5 = -1;
                    /* catch() { ... } // from try @ 00aeaa30 with catch @ 00aeaf00 */
  }
  else {
    do {
      __src = (void *)plVar7[5];
      iVar5 = (int)(short)plVar7[4];
      local_78 = 0;
      uStack_70 = 0;
      __n = plVar7[6] - (long)__src;
      local_80 = 0;
      if (__n == 0) {
        pwVar6 = (wchar_t *)0x0;
                    /* try { // try from 00aeae98 to 00beae9b has its CatchHandler @ 00aeaf1c */
        __s = (wchar_t *)0x0;
      }
      else {
        if ((long)__n < 0) {
                    /* catch() { ... } // from try @ 00aeab90 with catch @ 00aeaf48 */
                    /* catch() { ... } // from try @ 00aeabf0 with catch @ 00aeaf4c */
                    /* catch() { ... } // from try @ 00aeab20 with catch @ 00aeaf50 */
          if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470840(&local_80);
          }
          goto LAB_00aeaf90;
        }
        __s = (wchar_t *)_Znwm(__n);
        pwVar6 = (wchar_t *)((long)__s + __n);
        memcpy(__s,__src,__n);
      }
                    /* try { // try from 00aeaeac to 00beaeaf has its CatchHandler @ 00aeaed4 */
      pwVar4 = wmemchr(__s,param_2 + L'\xc4653600',(long)pwVar6 - (long)__s >> 2);
      if (__s != (wchar_t *)0x0) {
                    /* try { // try from 00aeaec0 to 00beaec3 has its CatchHandler @ 00aeaecc */
                    /* catch() { ... } // from try @ 00aead14 with catch @ 00aeaec4
                       try { // try from 00aeaec4 to 00beaf83 has its CatchHandler @ 00aea974 */
        _ZdlPv(__s);
      }
                    /* catch() { ... } // from try @ 00aeaca8 with catch @ 00aeaec8 */
      if (pwVar4 != (wchar_t *)0x0 && pwVar4 != pwVar6) goto LAB_00aeaf0c;
                    /* catch() { ... } // from try @ 00aead60 with catch @ 00aeaecc
                       catch() { ... } // from try @ 00aeaec0 with catch @ 00aeaecc */
                    /* catch() { ... } // from try @ 00aeaac0 with catch @ 00aeaed0 */
      plVar2 = (long *)plVar7[1];
      plVar8 = plVar7;
      if ((long *)plVar7[1] == (long *)0x0) {
        do {
          plVar7 = (long *)plVar8[2];
                    /* catch() { ... } // from try @ 00aeaa88 with catch @ 00aeaeec */
          bVar3 = (long *)*plVar7 != plVar8;
          plVar8 = plVar7;
                    /* catch() { ... } // from try @ 00aeaa3c with catch @ 00aeaef0 */
        } while (bVar3);
      }
      else {
        do {
                    /* catch() { ... } // from try @ 00aeacf4 with catch @ 00aeaed4
                       catch() { ... } // from try @ 00aeaeac with catch @ 00aeaed4 */
          plVar7 = plVar2;
          plVar2 = (long *)*plVar7;
        } while ((long *)*plVar7 != (long *)0x0);
      }
    } while (plVar7 != (long *)(param_1 + 0x33c8));
    iVar5 = -1;
  }
LAB_00aeaf0c:
                    /* catch() { ... } // from try @ 00aeac38 with catch @ 00aeaf10 */
                    /* catch() { ... } // from try @ 00aeaa20 with catch @ 00aeaf14 */
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aeac84 with catch @ 00aeaf1c
                       catch() { ... } // from try @ 00aeae98 with catch @ 00aeaf1c */
                    /* catch() { ... } // from try @ 00aea9f4 with catch @ 00aeaf20 */
                    /* catch() { ... } // from try @ 00aea9c0 with catch @ 00aeaf3c */
    return iVar5;
  }
LAB_00aeaf90:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
