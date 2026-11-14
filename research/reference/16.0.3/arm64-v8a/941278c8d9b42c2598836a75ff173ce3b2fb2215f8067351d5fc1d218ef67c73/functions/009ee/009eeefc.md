# 009eeefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009eeefc",
  "name": "FUN_009eeefc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51229530b9b277e18c6982bfa682b750421647200b8782d8e187049447722ea4",
  "source_text_sha256": "51229530b9b277e18c6982bfa682b750421647200b8782d8e187049447722ea4"
}
~~~

## 呼び出し元

- [009ef138](../009ef/009ef138.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [004413ec](../00441/004413ec.md)
- [009eeb3c](../009ee/009eeb3c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59100](../00c59/00c59100.md)

## 疑似コード / UTF-8 3677 bytes

~~~c

void FUN_009eeefc(long *param_1,long param_2,undefined8 param_3)

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
  
                    /* try { // try from 009eeefc to 00aeef0b has its CatchHandler @ 009f0734 */
                    /* try { // try from 009eef0c to 00aeef17 has its CatchHandler @ 009f0714 */
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
                    /* try { // try from 009eef58 to 00aeef5f has its CatchHandler @ 009f03dc */
  lVar4 = FUN_004413ec(param_2 + 0x10,local_80);
                    /* try { // try from 009eef60 to 00aeef6f has its CatchHandler @ 009f06d4 */
  if (param_2 + 0x18 == lVar4) {
    lVar4 = 0;
  }
  else {
    lVar4 = *(long *)(lVar4 + 0x38);
                    /* try { // try from 009eef70 to 00aeef7b has its CatchHandler @ 009f06b4 */
    if (*(int *)(lVar4 + 8) != 7) {
      lVar4 = 0;
    }
  }
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* try { // try from 009eef98 to 00aef103 has its CatchHandler @ 009ee1b8 */
  plVar11 = *(long **)(lVar4 + 0x10);
  if (plVar11 != (long *)(lVar4 + 0x18)) {
    do {
      iVar3 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (plVar11 + 4,0,10);
      lVar10 = plVar11[7];
      uVar5 = 0;
      if ((lVar10 == 0) || (*(int *)(lVar10 + 8) != 7)) goto LAB_009ef0d4;
      plVar9 = (long *)param_1[1];
      plVar8 = param_1 + 1;
      while (plVar12 = plVar8, plVar9 != (long *)0x0) {
        while (plVar6 = plVar9, plVar8 = plVar6, (int)plVar6[4] <= iVar3) {
          if (iVar3 <= (int)plVar6[4]) goto LAB_009ef084;
          plVar9 = (long *)plVar6[1];
          if ((long *)plVar6[1] == (long *)0x0) {
            plVar12 = plVar6 + 1;
            goto LAB_009ef02c;
          }
        }
        plVar9 = (long *)*plVar6;
      }
LAB_009ef02c:
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
      FUN_0043bf04(param_1[1],plVar8);
      param_1[2] = param_1[2] + 1;
LAB_009ef084:
      uVar7 = FUN_009eeb3c(plVar6 + 5,lVar10,param_3);
      if ((uVar7 & 1) == 0) {
        uVar5 = 0;
        goto LAB_009ef0d4;
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
LAB_009ef0d4:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* try { // try from 009ef104 to 00aef10b has its CatchHandler @ 009f03d4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~
