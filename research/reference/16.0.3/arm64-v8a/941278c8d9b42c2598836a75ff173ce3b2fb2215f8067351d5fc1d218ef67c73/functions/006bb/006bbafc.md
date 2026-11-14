# 006bbafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "006bbafc",
  "name": "FUN_006bbafc",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3cdf8cdf387af11326651d34dd3f91097d7d24ffc1b16ad928f2c28f9e61378",
  "source_text_sha256": "e3cdf8cdf387af11326651d34dd3f91097d7d24ffc1b16ad928f2c28f9e61378"
}
~~~

## 呼び出し元

- [00ae027c](../00ae0/00ae027c.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c59130](../00c59/00c59130.md)

## 疑似コード / UTF-8 4583 bytes

~~~c

bool FUN_006bbafc(int param_1,int param_2)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  ulong uVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
  lVar2 = FUN_008524fc();
  plVar4 = *(long **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
  do {
    if (plVar4 == (long *)0x0) {
      return false;
    }
    if (*(int *)((long)plVar4 + 0x1c) <= param_1) {
      if (param_1 <= *(int *)((long)plVar4 + 0x1c)) {
        uVar1 = 0;
        do {
          uVar5 = uVar1;
          lVar2 = FUN_008524fc();
          puVar6 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
          if (puVar6 == (undefined8 *)0x0) {
            puVar8 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
            puVar9 = puVar8;
          }
          else {
            do {
                    /* try { // try from 006bbbd8 to 007bc193 has its CatchHandler @ 006bc2cc */
              while (puVar3 = puVar6, puVar8 = puVar3, *(int *)((long)puVar3 + 0x1c) <= param_1) {
                if (param_1 <= *(int *)((long)puVar3 + 0x1c)) goto code_r0x006bbc58;
                puVar6 = (undefined8 *)puVar3[1];
                if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
                  puVar9 = puVar3 + 1;
                  goto LAB_006bbbf8;
                }
              }
                    /* try { // try from 006bbbcc to 007bbbd3 has its CatchHandler @ 006bc2c8 */
              puVar6 = (undefined8 *)*puVar3;
              puVar9 = puVar3;
            } while ((undefined8 *)*puVar3 != (undefined8 *)0x0);
          }
LAB_006bbbf8:
          puVar3 = (undefined8 *)_Znwm(0x290);
          *(int *)((long)puVar3 + 0x1c) = param_1;
          memset(puVar3 + 4,0,0x26c);
          *puVar3 = 0;
          puVar3[1] = 0;
          puVar3[2] = puVar8;
          *puVar9 = puVar3;
          lVar7 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar2);
          puVar6 = puVar3;
          if (lVar7 != 0) {
            *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar2) = lVar7;
            puVar6 = (undefined8 *)*puVar9;
          }
          FUN_0043bf04(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2),puVar6);
          *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) =
               *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) + 1;
code_r0x006bbc58:
          if (*(int *)((long)puVar3 + uVar5 * 0x38 + 0x24) == param_2) {
            lVar2 = FUN_008524fc();
            puVar6 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
            if (puVar6 == (undefined8 *)0x0) {
              puVar8 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
              puVar9 = puVar8;
            }
            else {
              do {
                while (puVar3 = puVar6, puVar8 = puVar3, *(int *)((long)puVar3 + 0x1c) <= param_1) {
                  if (param_1 <= *(int *)((long)puVar3 + 0x1c)) goto code_r0x006bbb90;
                  puVar6 = (undefined8 *)puVar3[1];
                  if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
                    puVar9 = puVar3 + 1;
                    goto LAB_006bbcb0;
                  }
                }
                puVar6 = (undefined8 *)*puVar3;
                puVar9 = puVar3;
              } while ((undefined8 *)*puVar3 != (undefined8 *)0x0);
            }
LAB_006bbcb0:
            puVar3 = (undefined8 *)_Znwm(0x290);
            *(int *)((long)puVar3 + 0x1c) = param_1;
            memset(puVar3 + 4,0,0x26c);
            *puVar3 = 0;
            puVar3[1] = 0;
            puVar3[2] = puVar8;
            *puVar9 = puVar3;
            lVar7 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar2);
            puVar6 = puVar3;
            if (lVar7 != 0) {
              *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar2) = lVar7;
              puVar6 = (undefined8 *)*puVar9;
            }
            FUN_0043bf04(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2),puVar6);
            *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) =
                 *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) + 1;
code_r0x006bbb90:
            if (*(int *)(puVar3 + uVar5 * 7 + 0xb) == 1) {
              return true;
            }
          }
          uVar1 = uVar5 + 1;
          if (uVar5 + 1 == 0xb) {
            return uVar5 < 10;
          }
        } while( true );
      }
                    /* try { // try from 006bbb64 to 007bbb77 has its CatchHandler @ 006bc2a8 */
      plVar4 = plVar4 + 1;
    }
    plVar4 = (long *)*plVar4;
  } while( true );
}

~~~
