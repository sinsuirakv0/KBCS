# 00aeae8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aeae8c",
  "name": "FUN_00aeae8c",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9e30ac2e79a38df647a0d0f704a993fabfad68e7bc31eed196c724a92594b88",
  "source_text_sha256": "f9e30ac2e79a38df647a0d0f704a993fabfad68e7bc31eed196c724a92594b88"
}
~~~

## 呼び出し元

- [00acecc4](../00ace/00acecc4.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c58520](../00c58/00c58520.md)

## 疑似コード / UTF-8 4873 bytes

~~~c

int FUN_00aeae8c(long param_1,int param_2)

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
                    /* catch() { ... } // from try @ 00aeabe4 with catch @ 00aeaf9c */
  }
  else {
    do {
      __src = (void *)plVar7[5];
      iVar5 = (int)(short)plVar7[4];
      local_78 = 0;
      uStack_70 = 0;
                    /* try { // try from 00aeaf00 to 00beaf03 has its CatchHandler @ 00aeaf28 */
      __n = plVar7[6] - (long)__src;
      local_80 = 0;
      if (__n == 0) {
        pwVar6 = (wchar_t *)0x0;
        __s = (wchar_t *)0x0;
      }
      else {
        if ((long)__n < 0) {
          if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470880(&local_80);
          }
          goto LAB_00aeb02c;
        }
                    /* try { // try from 00aeaf14 to 00beaf17 has its CatchHandler @ 00aeaf20 */
        __s = (wchar_t *)_Znwm(__n);
                    /* catch() { ... } // from try @ 00aead68 with catch @ 00aeaf18
                       try { // try from 00aeaf18 to 00beafd7 has its CatchHandler @ 00aea9c8 */
                    /* catch() { ... } // from try @ 00aeacfc with catch @ 00aeaf1c */
                    /* catch() { ... } // from try @ 00aeadb4 with catch @ 00aeaf20
                       catch() { ... } // from try @ 00aeaf14 with catch @ 00aeaf20 */
                    /* catch() { ... } // from try @ 00aeab14 with catch @ 00aeaf24 */
        pwVar6 = (wchar_t *)((long)__s + __n);
                    /* catch() { ... } // from try @ 00aead48 with catch @ 00aeaf28
                       catch() { ... } // from try @ 00aeaf00 with catch @ 00aeaf28 */
        memcpy(__s,__src,__n);
      }
                    /* catch() { ... } // from try @ 00aeaadc with catch @ 00aeaf40 */
                    /* catch() { ... } // from try @ 00aeaa90 with catch @ 00aeaf44 */
      pwVar4 = wmemchr(__s,param_2 + L'\xc4653600',(long)pwVar6 - (long)__s >> 2);
                    /* catch() { ... } // from try @ 00aeaa84 with catch @ 00aeaf54 */
      if (__s != (wchar_t *)0x0) {
        _ZdlPv(__s);
      }
                    /* catch() { ... } // from try @ 00aeac8c with catch @ 00aeaf64 */
      if (pwVar4 != (wchar_t *)0x0 && pwVar4 != pwVar6) goto LAB_00aeafa8;
                    /* catch() { ... } // from try @ 00aeaa74 with catch @ 00aeaf68 */
      plVar2 = (long *)plVar7[1];
      plVar8 = plVar7;
      if ((long *)plVar7[1] == (long *)0x0) {
        do {
          plVar7 = (long *)plVar8[2];
          bVar3 = (long *)*plVar7 != plVar8;
          plVar8 = plVar7;
                    /* catch() { ... } // from try @ 00aeaa14 with catch @ 00aeaf90 */
        } while (bVar3);
      }
      else {
        do {
                    /* catch() { ... } // from try @ 00aeacd8 with catch @ 00aeaf70
                       catch() { ... } // from try @ 00aeaeec with catch @ 00aeaf70 */
          plVar7 = plVar2;
                    /* catch() { ... } // from try @ 00aeaa48 with catch @ 00aeaf74 */
          plVar2 = (long *)*plVar7;
        } while ((long *)*plVar7 != (long *)0x0);
      }
                    /* try { // try from 00aeaeec to 00beaeef has its CatchHandler @ 00aeaf70 */
    } while (plVar7 != (long *)(param_1 + 0x33c8));
                    /* catch() { ... } // from try @ 00aeac44 with catch @ 00aeafa0 */
    iVar5 = -1;
  }
LAB_00aeafa8:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aeb27c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb388 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb55c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb5ec with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb680 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb710 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb8e4 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb92c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebbc4 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebc60 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebe5c with catch @ 00aeafd8 */
    return iVar5;
  }
LAB_00aeb02c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
