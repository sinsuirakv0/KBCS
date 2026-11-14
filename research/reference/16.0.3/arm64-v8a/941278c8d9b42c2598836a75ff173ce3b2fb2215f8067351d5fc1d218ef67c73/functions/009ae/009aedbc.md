# 009aedbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009aedbc",
  "name": "FUN_009aedbc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a9d42345128faa149b43f47f07abc8b41200185a2164bf18121b21a21f1a197",
  "source_text_sha256": "2a9d42345128faa149b43f47f07abc8b41200185a2164bf18121b21a21f1a197"
}
~~~

## 呼び出し元

- [0061343c](../00613/0061343c.md)

## 呼び出し先

- [009b6c94](../009b6/009b6c94.md)
- [009b6cd4](../009b6/009b6cd4.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 2232 bytes

~~~c

void FUN_009aedbc(undefined2 *param_1,undefined8 *param_2,int param_3)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  
                    /* try { // try from 009aedc8 to 00aaedd7 has its CatchHandler @ 009aee18 */
                    /* try { // try from 009aedd8 to 00aaee73 has its CatchHandler @ 009aed3c */
  lVar5 = tpidr_el0;
  lVar8 = *(long *)(lVar5 + 0x28);
  puVar1 = (undefined8 *)*param_2;
  puVar3 = (undefined8 *)param_2[1];
  do {
    if (puVar1 == puVar3) {
      *param_1 = 0;
      if (*(long *)(lVar5 + 0x28) == lVar8) {
        return;
      }
LAB_009aeee4:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c54d60(1,plVar4 + 1);
    }
    iVar6 = FUN_009b6c94(uVar2);
                    /* catch() { ... } // from try @ 009aedc8 with catch @ 009aee18 */
    if ((plVar4 != (long *)0x0) && (lVar7 = FUN_00c54d90(0xffffffffffffffff,plVar4 + 1), lVar7 == 0)
       ) {
                    /* catch() { ... } // from try @ 009aedb4 with catch @ 009aee30 */
      (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* catch() { ... } // from try @ 009aed8c with catch @ 009aee44 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    if (iVar6 == param_3) {
      if (*(long *)(lVar5 + 0x28) == lVar8) {
                    /* try { // try from 009aee9c to 00aaf007 has its CatchHandler @ 009aee9c
                       catch() { ... } // from try @ 009aee9c with catch @ 009aee9c
                       catch() { ... } // from try @ 009af0c8 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af350 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af444 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af664 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af700 with catch @ 009aee9c */
        FUN_009b6cd4(param_1,uVar2);
        return;
      }
      goto LAB_009aeee4;
    }
    puVar1 = puVar1 + 2;
  } while( true );
}

~~~
