# 009edefc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009edefc",
  "name": "FUN_009edefc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90cdd9e44e04f9ae6daad79aa190d88e5d60dcdb7414f6e5bd83da7b102aa1d7",
  "source_text_sha256": "90cdd9e44e04f9ae6daad79aa190d88e5d60dcdb7414f6e5bd83da7b102aa1d7"
}
~~~

## 呼び出し元

- [009ee138](../009ee/009ee138.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [0044108c](../00441/0044108c.md)
- [009edb3c](../009ed/009edb3c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58060](../00c58/00c58060.md)

## 疑似コード / UTF-8 3677 bytes

~~~c

void FUN_009edefc(long *param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  bool bVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  long *plVar9;
  long lVar10;
  long *plVar11;
  long *plVar12;
  byte local_80 [16];
  void *local_70;
  long local_68;
  
                    /* try { // try from 009edefc to 00aedf0b has its CatchHandler @ 009ef734 */
                    /* try { // try from 009edf0c to 00aedf17 has its CatchHandler @ 009ef714 */
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  local_80[0] = 0x10;
  local_80[9] = 0;
  local_80[1] = 0x42;
  local_80[2] = 0x6f;
  local_80[3] = 0x6e;
  local_80[4] = 0x75;
  local_80[5] = 0x73;
  local_80[6] = 0x4e;
  local_80[7] = 0x75;
  local_80[8] = 0x6d;
                    /* try { // try from 009edf58 to 00aedf5f has its CatchHandler @ 009ef3dc */
  lVar4 = FUN_0044108c(param_2 + 0x10,local_80);
                    /* try { // try from 009edf60 to 00aedf6f has its CatchHandler @ 009ef6d4 */
  if (param_2 + 0x18 == lVar4) {
    lVar4 = 0;
  }
  else {
    lVar4 = *(long *)(lVar4 + 0x38);
                    /* try { // try from 009edf70 to 00aedf7b has its CatchHandler @ 009ef6b4 */
    if (*(int *)(lVar4 + 8) != 7) {
      lVar4 = 0;
    }
  }
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* try { // try from 009edf98 to 00aee103 has its CatchHandler @ 009ed1b8 */
  plVar11 = *(long **)(lVar4 + 0x10);
  if (plVar11 != (long *)(lVar4 + 0x18)) {
    do {
      iVar3 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (plVar11 + 4,0,10);
      lVar10 = plVar11[7];
      uVar5 = 0;
      if ((lVar10 == 0) || (*(int *)(lVar10 + 8) != 7)) goto LAB_009ee0d4;
      plVar9 = (long *)param_1[1];
      plVar8 = param_1 + 1;
      while (plVar12 = plVar8, plVar9 != (long *)0x0) {
        while (plVar6 = plVar9, plVar8 = plVar6, (int)plVar6[4] <= iVar3) {
          if (iVar3 <= (int)plVar6[4]) goto LAB_009ee084;
          plVar9 = (long *)plVar6[1];
          if ((long *)plVar6[1] == (long *)0x0) {
            plVar12 = plVar6 + 1;
            goto LAB_009ee02c;
          }
        }
        plVar9 = (long *)*plVar6;
      }
LAB_009ee02c:
      plVar6 = (long *)_Znwm(0x48);
      *plVar6 = 0;
      plVar6[1] = 0;
      plVar6[7] = 0;
      plVar6[8] = 0;
      plVar6[6] = 0;
      plVar6[2] = (long)plVar8;
      *plVar12 = (long)plVar6;
      plVar9 = (long *)*param_1;
      *(int *)(plVar6 + 4) = iVar3;
      *(undefined4 *)(plVar6 + 5) = 0;
      plVar8 = plVar6;
      if (*plVar9 != 0) {
        *param_1 = *plVar9;
        plVar8 = (long *)*plVar12;
      }
      FUN_0043bba4(param_1[1],plVar8);
      param_1[2] = param_1[2] + 1;
LAB_009ee084:
      uVar7 = FUN_009edb3c(plVar6 + 5,lVar10,param_3);
      if ((uVar7 & 1) == 0) {
        uVar5 = 0;
        goto LAB_009ee0d4;
      }
      plVar8 = (long *)plVar11[1];
      plVar9 = plVar11;
      if ((long *)plVar11[1] == (long *)0x0) {
        do {
          plVar11 = (long *)plVar9[2];
          bVar2 = (long *)*plVar11 != plVar9;
          plVar9 = plVar11;
        } while (bVar2);
      }
      else {
        do {
          plVar11 = plVar8;
          plVar8 = (long *)*plVar11;
        } while ((long *)*plVar11 != (long *)0x0);
      }
    } while (plVar11 != (long *)(lVar4 + 0x18));
  }
  uVar5 = 1;
LAB_009ee0d4:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* try { // try from 009ee104 to 00aee10b has its CatchHandler @ 009ef3d4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~
