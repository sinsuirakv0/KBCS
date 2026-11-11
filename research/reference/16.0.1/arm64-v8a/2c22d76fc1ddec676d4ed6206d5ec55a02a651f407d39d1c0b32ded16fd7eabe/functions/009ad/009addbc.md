# 009addbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009addbc",
  "name": "FUN_009addbc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c99a4516960d90324aafebcc8598f78425cd264e97e57b2c18db7be50cc60cc0",
  "source_text_sha256": "c99a4516960d90324aafebcc8598f78425cd264e97e57b2c18db7be50cc60cc0"
}
~~~

## 呼び出し元

- [0061304c](../00613/0061304c.md)

## 呼び出し先

- [009b5c94](../009b5/009b5c94.md)
- [009b5cd4](../009b5/009b5cd4.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 2232 bytes

~~~c

void FUN_009addbc(undefined2 *param_1,undefined8 *param_2,int param_3)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  
                    /* try { // try from 009addc4 to 00aaddd3 has its CatchHandler @ 009ade14 */
                    /* try { // try from 009addd4 to 00aade6f has its CatchHandler @ 009add38 */
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
LAB_009adee4:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c53cd0(1,plVar4 + 1);
    }
                    /* catch() { ... } // from try @ 009addc4 with catch @ 009ade14 */
    iVar6 = FUN_009b5c94(uVar2);
                    /* catch() { ... } // from try @ 009addb0 with catch @ 009ade2c */
    if ((plVar4 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar7 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* catch() { ... } // from try @ 009add88 with catch @ 009ade40 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    if (iVar6 == param_3) {
                    /* try { // try from 009ade98 to 00aae003 has its CatchHandler @ 009ade98
                       catch() { ... } // from try @ 009ade98 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae0c4 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae34c with catch @ 009ade98
                       catch() { ... } // from try @ 009ae440 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae660 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae6fc with catch @ 009ade98 */
      if (*(long *)(lVar5 + 0x28) == lVar8) {
        FUN_009b5cd4(param_1,uVar2);
        return;
      }
      goto LAB_009adee4;
    }
    puVar1 = puVar1 + 2;
  } while( true );
}

~~~
