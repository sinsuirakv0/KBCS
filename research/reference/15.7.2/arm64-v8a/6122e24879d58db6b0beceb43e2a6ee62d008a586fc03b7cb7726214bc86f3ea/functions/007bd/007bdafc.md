# 007bdafc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007bdafc.md)

## 関数情報

~~~json
{
  "address": "007bdafc",
  "name": "FUN_007bdafc",
  "size": 1600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43c813bd32f3ae76a0e41bcdffcbf2e9f2418161518b431c6c8ade0c7c4650da",
  "source_text_sha256": "43c813bd32f3ae76a0e41bcdffcbf2e9f2418161518b431c6c8ade0c7c4650da"
}
~~~
## 呼び出し元

- [007c9cac](../007c9/007c9cac.md)
- [007c9d9c](../007c9/007c9d9c.md)

## 呼び出し先

- [00469fac](../00469/00469fac.md)
- [005bfb9c](../005bf/005bfb9c.md)
- [005bfe78](../005bf/005bfe78.md)
- [005c01d4](../005c0/005c01d4.md)
- [005c3468](../005c3/005c3468.md)
- [005d996c](../005d9/005d996c.md)
- [007086f4](../00708/007086f4.md)
- [00708b44](../00708/00708b44.md)
- [00733548](../00733/00733548.md)
- [00796dfc](../00796/00796dfc.md)
- [00798650](../00798/00798650.md)
- [00798f70](../00798/00798f70.md)
- [0079942c](../00799/0079942c.md)
- [007999cc](../00799/007999cc.md)
- [007ab264](../007ab/007ab264.md)
- [007cf4b0](../007cf/007cf4b0.md)
- [007cf950](../007cf/007cf950.md)
- [007cf984](../007cf/007cf984.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [007cffa8](../007cf/007cffa8.md)
- [007eb290](../007eb/007eb290.md)
- [007f96a4](../007f9/007f96a4.md)
- [0081f580](../0081f/0081f580.md)
- [00846bc4](../00846/00846bc4.md)
- [008a36b4](../008a3/008a36b4.md)
- [009a9454](../009a9/009a9454.md)
- [009bd60c](../009bd/009bd60c.md)
- [00a5c504](../00a5c/00a5c504.md)
- [00a5c558](../00a5c/00a5c558.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdd8e0](../00bdd/00bdd8e0.md)
- [00bdd8f0](../00bdd/00bdd8f0.md)

## 関連文字列（未確認候補）

~~~text
"MapID"
"StageIdx"
"StageLv"
"ex_id"
"ex_type"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~
## 疑似コード 1/1 / UTF-8 8688 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_007bdafc(long param_1,undefined4 param_2,undefined4 param_3)

{
  int *piVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  ulong uVar8;
  long lVar9;
  undefined8 uVar10;
  long lVar11;
  undefined1 auVar12 [16];
  undefined1 auVar13 [16];
  undefined1 auVar14 [16];
  undefined4 local_140 [2];
  char *local_138;
  char *local_128;
  undefined4 local_120 [2];
  undefined8 local_118;
  char *local_108;
  undefined4 local_100 [2];
  undefined8 local_f8;
  char *local_e8;
  undefined4 local_e0 [2];
  undefined8 local_d8;
  char *local_c8;
  undefined4 local_c0 [2];
  undefined8 local_b8;
  char *local_a8;
  undefined4 local_a0 [2];
  undefined8 local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  FUN_009a9454(param_1 + 0x8c0,param_3);
  FUN_007ab264(param_1,param_2);
  iVar4 = FUN_007cf4b0(0);
  if (iVar4 == -0xb) {
    iVar4 = FUN_007cf984(0);
    lVar9 = *(long *)((long)&QWORD_00382fc4 + param_1 + 4);
    iVar5 = FUN_007cfaa0();
    iVar6 = FUN_007cfcd8();
    if (*(short *)(lVar9 + (long)iVar4 * 0x180 + (long)iVar5 * 8 + (long)iVar6 * 2) < 9999) {
      iVar4 = FUN_007cf984(0);
      lVar9 = *(long *)((long)&QWORD_00382fc4 + param_1 + 4);
      iVar5 = FUN_007cfaa0();
      lVar9 = lVar9 + (long)iVar4 * 0x180 + (long)iVar5 * 8;
      uVar8 = FUN_007cfcd8();
      uVar8 = -(uVar8 >> 0x1f & 1) & 0xfffffffe00000000 | (uVar8 & 0xffffffff) << 1;
      *(short *)(lVar9 + uVar8) = *(short *)(lVar9 + uVar8) + 1;
    }
  }
  uVar8 = FUN_007cffa8();
  if ((uVar8 & 1) == 0) {
    local_128 = "sec1_type";
    local_120[0] = 0;
    local_118 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,4);
    local_138 = "MapID";
    firebase::Variant::operator=((Variant *)local_120,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    iVar4 = FUN_007cf950(0);
    local_108 = "sec1_id";
    local_100[0] = 0;
    local_f8 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,1);
    local_138 = (char *)(long)iVar4;
    firebase::Variant::operator=((Variant *)local_100,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    local_e8 = "sec2_type";
    local_e0[0] = 0;
    local_d8 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,4);
    local_138 = "StageIdx";
    firebase::Variant::operator=((Variant *)local_e0,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    iVar4 = FUN_007cfaa0();
    local_c8 = "sec2_id";
    local_c0[0] = 0;
    local_b8 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,1);
    local_138 = (char *)(long)iVar4;
    firebase::Variant::operator=((Variant *)local_c0,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    local_a8 = "ex_type";
    local_a0[0] = 0;
    local_98 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,4);
    local_138 = "StageLv";
    firebase::Variant::operator=((Variant *)local_a0,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    iVar4 = FUN_007cfcd8();
    local_88 = "ex_id";
    local_80[0] = 0;
    local_78 = 0;
    local_140[0] = 0;
    firebase::Variant::Clear((Variant *)local_140,1);
    local_138 = (char *)(long)iVar4;
    firebase::Variant::operator=((Variant *)local_80,(Variant *)local_140);
    firebase::Variant::Clear((Variant *)local_140,0);
    lVar9 = FUN_0081f580();
    FUN_00846bc4(*(undefined8 *)(lVar9 + 0x21c8),0x1317f09,*(undefined4 *)(param_1 + 0x41c),
                 &local_128,6);
    firebase::Variant::Clear((Variant *)local_80,0);
    firebase::Variant::Clear((Variant *)local_a0,0);
    firebase::Variant::Clear((Variant *)local_c0,0);
    firebase::Variant::Clear((Variant *)local_e0,0);
    firebase::Variant::Clear((Variant *)local_100,0);
    firebase::Variant::Clear((Variant *)local_120,0);
  }
  piVar1 = (int *)(param_1 + 0x4a5b8);
  uVar7 = FUN_005bfb9c(1);
  if (((((uVar7 & 1) != 0) && (*(char *)(param_1 + 0x32e9) == '\0')) &&
      (uVar8 = FUN_008a36b4(param_1 + 0x1f90,1), (uVar8 & 1) == 0)) &&
     (uVar8 = FUN_00708b44(param_1 + 0x1408,1), (uVar8 & 1) == 0)) {
    uVar10 = *(undefined8 *)piVar1;
    auVar12._8_8_ = uVar10;
    auVar12._0_8_ = uVar10;
    auVar13 = NEON_ushl(auVar12,_DAT_002b16f0,8);
    auVar12 = NEON_ushl(auVar12,_DAT_002b10e0,8);
    uVar8 = NEON_ushl(CONCAT44(CONCAT13(auVar12[0xb] ^ auVar13[0xb],
                                        CONCAT12(auVar12[10] ^ auVar13[10],
                                                 CONCAT11(auVar12[9] ^ auVar13[9],
                                                          auVar12[8] ^ auVar13[8]))),
                               CONCAT13(auVar12[3] ^ auVar13[3],
                                        CONCAT12(auVar12[2] ^ auVar13[2],
                                                 CONCAT11(auVar12[1] ^ auVar13[1],
                                                          auVar12[0] ^ auVar13[0])))),DAT_002b29c8,4
                     );
    *piVar1 = (((uint)(byte)((ulong)uVar10 >> 0x38) ^ (uint)uVar10) & 0xff |
               ((uint)((ulong)uVar10 >> 0x20) ^ (uint)uVar10 >> 0x18) << 0x18 |
               (uint)(uVar8 & 0xff00000000ff00) | (uint)((uVar8 & 0xff00000000ff00) >> 0x20)) - 1;
    FUN_005c3468(piVar1);
  }
  FUN_005c01d4(1,uVar7 & 1);
  uVar7 = FUN_005bfb9c(4);
  if ((((uVar7 & 1) != 0) && (*(char *)(param_1 + 0x32e9) == '\0')) &&
     ((uVar8 = FUN_008a36b4(param_1 + 0x1f90,4), (uVar8 & 1) == 0 &&
      (uVar8 = FUN_00708b44(param_1 + 0x1408,4), (uVar8 & 1) == 0)))) {
    uVar10 = *(undefined8 *)(param_1 + 0x4a5d0);
    auVar13._8_8_ = uVar10;
    auVar13._0_8_ = uVar10;
    auVar14 = NEON_ushl(auVar13,_DAT_002b16f0,8);
    auVar12 = NEON_ushl(auVar13,_DAT_002b10e0,8);
    uVar8 = NEON_ushl(CONCAT44(CONCAT13(auVar12[0xb] ^ auVar14[0xb],
                                        CONCAT12(auVar12[10] ^ auVar14[10],
                                                 CONCAT11(auVar12[9] ^ auVar14[9],
                                                          auVar12[8] ^ auVar14[8]))),
                               CONCAT13(auVar12[3] ^ auVar14[3],
                                        CONCAT12(auVar12[2] ^ auVar14[2],
                                                 CONCAT11(auVar12[1] ^ auVar14[1],
                                                          auVar12[0] ^ auVar14[0])))),DAT_002b29c8,4
                     );
    *(uint *)(param_1 + 0x4a5d0) =
         (((uint)(byte)((ulong)uVar10 >> 0x38) ^ (uint)uVar10) & 0xff |
          ((uint)((ulong)uVar10 >> 0x20) ^ (uint)uVar10 >> 0x18) << 0x18 |
          (uint)(uVar8 & 0xff00000000ff00) | (uint)((uVar8 & 0xff00000000ff00) >> 0x20)) - 1;
    FUN_005c3468();
  }
  FUN_005c01d4(4,uVar7 & 1);
  FUN_005d996c(param_1,1);
  FUN_005bfe78();
  FUN_00796dfc(param_1);
  uVar8 = FUN_00733548(param_1,2,0);
  if ((uVar8 & 1) != 0) {
    *(undefined1 *)(param_1 + 0x1ee9) = 1;
  }
  *(undefined4 *)(param_1 + 0x900) = 1;
  FUN_00469fac();
  FUN_007086f4(param_1 + 0x1408);
  FUN_00798650(param_1);
  FUN_00798f70(param_1);
  FUN_0079942c(param_1);
  FUN_007999cc(param_1);
  iVar4 = *(int *)(BYTE_ARRAY_0032f921 + param_1 + 0x13);
  BYTE_ARRAY_003c3529[param_1 + 1] = 0;
  if (((iVar4 != 3) && (uVar8 = FUN_00a5c504(param_1 + 8), (uVar8 & 1) != 0)) &&
     ((*(int *)(param_1 + 0x4a660) == 0 && (uVar8 = FUN_00a5c558(param_1 + 8), (uVar8 & 1) != 0))))
  {
    lVar9 = 0;
    lVar11 = param_1 + (long)*(int *)(BYTE_ARRAY_0032f921 + param_1 + 0x13) * 200;
    do {
      pbVar2 = (byte *)(lVar11 + 0xd289 + lVar9);
      if (((uint)(*(byte *)(lVar11 + 0xd34e) ^ pbVar2[1]) << 0x10 |
           (uint)(*(byte *)(lVar11 + 0xd34f) ^ pbVar2[2]) << 0x18 |
           (uint)(*(byte *)(lVar11 + 0xd34d) ^ *pbVar2) << 8 |
          (uint)(*(byte *)(lVar11 + 0xd34c) ^ pbVar2[-1])) != 3) {
        BYTE_ARRAY_003c3529[param_1 + 1] = 1;
        break;
      }
      lVar9 = lVar9 + 4;
    } while (lVar9 != 0xc0);
  }
  FUN_007f96a4((long)&DWORD_00333aa8 + param_1,0x21,3);
  FUN_007eb290(param_1 + 0x333ae8);
  FUN_009bd60c(param_1);
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
