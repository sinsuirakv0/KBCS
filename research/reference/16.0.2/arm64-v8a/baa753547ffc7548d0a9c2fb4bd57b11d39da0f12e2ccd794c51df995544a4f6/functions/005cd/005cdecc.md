# 005cdecc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "005cdecc",
  "name": "FUN_005cdecc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29f394f33b25056d765975f62f67648a12640aa4c0f14cf6f531b69b8e02a09d",
  "source_text_sha256": "29f394f33b25056d765975f62f67648a12640aa4c0f14cf6f531b69b8e02a09d"
}
~~~

## 呼び出し元

- [005cd7f8](../005cd/005cd7f8.md)
- [005ce1f4](../005ce/005ce1f4.md)
- [005d58ac](../005d5/005d58ac.md)

## 呼び出し先

- [005d51f0](../005d5/005d51f0.md)
- [005d58ac](../005d5/005d58ac.md)
- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 3902 bytes

~~~c

char * FUN_005cdecc(long param_1,char *param_2,char *param_3)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined *puVar3;
  char *pcVar4;
  char *pcVar5;
  long *plVar6;
  long lVar7;
  long lVar8;
  char *pcVar9;
  long lVar10;
  long lVar11;
  
  lVar10 = *(long *)(param_1 + 0x38);
  pcVar4 = (char *)FUN_005d58ac();
  if (pcVar4 != param_2) {
    do {
      pcVar9 = pcVar4;
      pcVar4 = (char *)FUN_005d58ac(param_1,pcVar9,param_3);
    } while (pcVar4 != pcVar9);
    if (pcVar9 != param_2) {
      if (pcVar9 != param_3) {
        puVar1 = PTR__ZTVNSt6__ndk111__alternateIcEE_00c9b468 + 0x10;
        puVar2 = PTR__ZTVNSt6__ndk113__empty_stateIcEE_00c9b458 + 0x10;
        puVar3 = PTR__ZTVNSt6__ndk121__empty_non_own_stateIcEE_00c9b470 + 0x10;
        do {
          if (*pcVar9 != '|') {
            return pcVar9;
          }
          pcVar4 = pcVar9 + 1;
          lVar11 = *(long *)(param_1 + 0x38);
          pcVar5 = (char *)FUN_005d58ac(param_1,pcVar4,param_3);
          if (pcVar5 == pcVar4) goto LAB_005ce03c;
          do {
            pcVar9 = pcVar5;
                    /* try { // try from 005cdf88 to 006cdf8f has its CatchHandler @ 005ce008 */
            pcVar5 = (char *)FUN_005d58ac(param_1,pcVar9,param_3);
          } while (pcVar5 != pcVar9);
                    /* try { // try from 005cdfa0 to 006cdfa7 has its CatchHandler @ 005cdfc8 */
          if (pcVar9 == pcVar4) goto LAB_005ce03c;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdeb8 with catch @ 005cdfa8
                       try { // try from 005cdfa8 to 006ce08f has its CatchHandler @ 005cdc6c */
          plVar6 = (long *)_Znwm(0x18);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cddd0 with catch @ 005cdfac
                        */
          lVar7 = *(long *)(lVar11 + 8);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cde2c with catch @ 005cdfb0
                        */
          lVar8 = *(long *)(lVar10 + 8);
          *plVar6 = (long)puVar1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cddf0 with catch @ 005cdfb8
                        */
          plVar6[1] = lVar8;
          plVar6[2] = lVar7;
          *(long **)(lVar10 + 8) = plVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd48 with catch @ 005cdfc0
                        */
          *(undefined8 *)(lVar11 + 8) = 0;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cde58 with catch @ 005cdfc8
                       catch(type#1 @ 00000000) { ... } // from try @ 005cdfa0 with catch @ 005cdfc8
                        */
          plVar6 = (long *)_Znwm(0x10);
          lVar7 = *(long *)(param_1 + 0x38);
          *plVar6 = (long)puVar2;
          plVar6[1] = *(long *)(lVar7 + 8);
          *(long **)(lVar11 + 8) = plVar6;
          *(undefined8 *)(*(long *)(param_1 + 0x38) + 8) = 0;
          plVar6 = (long *)_Znwm(0x10);
          lVar7 = *(long *)(lVar11 + 8);
          lVar8 = *(long *)(param_1 + 0x38);
          *plVar6 = (long)puVar3;
          plVar6[1] = lVar7;
          *(long **)(lVar8 + 8) = plVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd68 with catch @ 005ce008
                       catch(type#1 @ 00000000) { ... } // from try @ 005cdf88 with catch @ 005ce008
                        */
          *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(lVar11 + 8);
        } while (pcVar9 != param_3);
      }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd24 with catch @ 005ce02c
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005cdd04 with catch @ 005ce030
                        */
      return param_3;
    }
  }
LAB_005ce03c:
                    /* WARNING: Subroutine does not return */
  FUN_005d51f0();
}

~~~
