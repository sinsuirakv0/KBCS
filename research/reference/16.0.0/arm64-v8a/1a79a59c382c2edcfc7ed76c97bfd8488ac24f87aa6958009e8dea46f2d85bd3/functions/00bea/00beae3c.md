# 00beae3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0175.md#review-2ffb8ce2bb43dbed24c2f00f8b605dca)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0003.md#review-2ffb8ce2bb43dbed24c2f00f8b605dca)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beae3c",
  "name": "FUN_00beae3c",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d1aafcb64aeaeab9acee9ec736366369bbacc0bf842e4ca385b91aeb41feb22",
  "source_text_sha256": "5d1aafcb64aeaeab9acee9ec736366369bbacc0bf842e4ca385b91aeb41feb22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beae3c",
        "00beb0fb"
      ]
    ],
    "bytes_sha256": "7ea56d5972a051beb45bb1723b0970a106d4c4eda3cd300874443a57388e77b1",
    "instruction_count": 176,
    "instruction_bytes": 704,
    "body_bytes": 704,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be4234](../00be4/00be4234.md)

## 呼び出し先

- [00beb0fc](../00beb/00beb0fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4056 bytes

~~~c

bool FUN_00beae3c(ushort *param_1,ushort *param_2)

{
  ushort uVar1;
  long lVar2;
  ushort uVar3;
  ushort uVar4;
  ulong uVar5;
  int iVar6;
  ushort uVar7;
  ushort *puVar8;
  long lVar9;
  ushort uVar10;
  ushort *puVar11;
  ushort *puVar12;
  long lVar13;
  ushort *puVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 1;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      uVar10 = param_1[1];
      uVar4 = *param_1;
      uVar1 = param_2[-1];
      if (uVar4 <= uVar10) {
        if (uVar10 <= uVar1) {
          return true;
        }
        param_1[1] = uVar1;
        param_2[-1] = uVar10;
        uVar4 = *param_1;
        if (param_1[1] < uVar4) {
          *param_1 = param_1[1];
          param_1[1] = uVar4;
          return true;
        }
        return true;
      }
      if (uVar1 < uVar10) {
        *param_1 = uVar1;
      }
      else {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        if (uVar4 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00beb0d0;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00beb0fc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beaed0;
    }
    uVar4 = *param_1;
    puVar12 = param_1 + 1;
    uVar10 = *puVar12;
    puVar8 = param_1 + 2;
    uVar1 = *puVar8;
    puVar11 = param_1;
    if (uVar10 < uVar4) {
      puVar14 = puVar8;
      uVar3 = uVar4;
      if (uVar10 <= uVar1) {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        uVar10 = uVar1;
        puVar11 = puVar12;
        goto joined_r0x00beb05c;
      }
    }
    else {
      uVar7 = uVar1;
      if (uVar10 <= uVar1) goto LAB_00beb074;
      *puVar12 = uVar1;
      *puVar8 = uVar10;
      puVar14 = puVar12;
      uVar3 = uVar10;
joined_r0x00beb05c:
      uVar7 = uVar10;
      if (uVar4 <= uVar1) goto LAB_00beb074;
    }
    *puVar11 = uVar1;
    *puVar14 = uVar4;
    uVar7 = uVar3;
LAB_00beb074:
    if (uVar7 <= param_2[-1]) {
      return true;
    }
    *puVar8 = param_2[-1];
    param_2[-1] = uVar7;
    uVar4 = *puVar8;
    uVar10 = *puVar12;
    if (uVar4 < uVar10) {
      uVar1 = *param_1;
      param_1[1] = uVar4;
      param_1[2] = uVar10;
      if (uVar4 < uVar1) {
        *param_1 = uVar4;
        param_1[1] = uVar1;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar5 < 2) {
    return true;
  }
  if (uVar5 == 2) {
    uVar4 = *param_1;
    if (uVar4 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00beb0d0:
    param_2[-1] = uVar4;
    return true;
  }
LAB_00beaed0:
  uVar4 = *param_1;
  puVar8 = param_1 + 1;
  uVar10 = *puVar8;
  puVar12 = param_1 + 2;
  uVar1 = *puVar12;
  puVar11 = param_1;
  if (uVar10 < uVar4) {
    puVar14 = puVar12;
    if (uVar10 <= uVar1) {
      *param_1 = uVar10;
      param_1[1] = uVar4;
      puVar11 = puVar8;
      goto joined_r0x00beafb0;
    }
  }
  else {
    if (uVar10 <= uVar1) goto LAB_00beafbc;
    *puVar8 = uVar1;
    *puVar12 = uVar10;
    puVar14 = puVar8;
joined_r0x00beafb0:
    if (uVar4 <= uVar1) goto LAB_00beafbc;
  }
  *puVar11 = uVar1;
  *puVar14 = uVar4;
LAB_00beafbc:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 6;
    puVar11 = param_1 + 3;
    do {
      puVar8 = puVar11;
      uVar4 = *puVar8;
      uVar10 = *puVar12;
      lVar13 = lVar9;
      if (uVar4 < uVar10) {
        do {
          lVar2 = lVar13 + -2;
          *(ushort *)((long)param_1 + lVar13) = uVar10;
          puVar11 = param_1;
          if (lVar2 == 0) goto LAB_00beafd8;
          uVar10 = *(ushort *)((long)param_1 + lVar13 + -4);
          lVar13 = lVar2;
        } while (uVar4 < uVar10);
        puVar11 = (ushort *)((long)param_1 + lVar2);
LAB_00beafd8:
        iVar6 = iVar6 + 1;
        *puVar11 = uVar4;
        if (iVar6 == 8) {
          return puVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 2;
      puVar11 = puVar8 + 1;
      puVar12 = puVar8;
    } while (puVar8 + 1 != param_2);
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beae3c"></a> `00beae3c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beae40"></a> `00beae40` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00beae44"></a> `00beae44` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00beae48"></a> `00beae48` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beae4c"></a> `00beae4c` | `08 fd 41 93` | asr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00beae50"></a> `00beae50` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beae54"></a> `00beae54` | `4c 01 00 54` | b.gt 0x00beae7c | `CONDITIONAL_JUMP`
<a id="insn-00beae58"></a> `00beae58` | `23 14 00 54` | b.cc 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beae5c"></a> `00beae5c` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beae60"></a> `00beae60` | `81 03 00 54` | b.ne 0x00beaed0 | `CONDITIONAL_JUMP`
<a id="insn-00beae64"></a> `00beae64` | `29 e0 5f 78` | ldurh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beae68"></a> `00beae68` | `08 00 40 79` | ldrh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beae6c"></a> `00beae6c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beae70"></a> `00beae70` | `62 13 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beae74"></a> `00beae74` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beae78"></a> `00beae78` | `96 00 00 14` | b 0x00beb0d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beae7c"></a> `00beae7c` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beae80"></a> `00beae80` | `60 01 00 54` | b.eq 0x00beaeac | `CONDITIONAL_JUMP`
<a id="insn-00beae84"></a> `00beae84` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beae88"></a> `00beae88` | `80 04 00 54` | b.eq 0x00beaf18 | `CONDITIONAL_JUMP`
<a id="insn-00beae8c"></a> `00beae8c` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00beae90"></a> `00beae90` | `01 02 00 54` | b.ne 0x00beaed0 | `CONDITIONAL_JUMP`
<a id="insn-00beae94"></a> `00beae94` | `24 08 00 d1` | sub x4,x1,#0x2 | `FALL_THROUGH`
<a id="insn-00beae98"></a> `00beae98` | `01 08 00 91` | add x1,x0,#0x2 | `FALL_THROUGH`
<a id="insn-00beae9c"></a> `00beae9c` | `02 10 00 91` | add x2,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00beaea0"></a> `00beaea0` | `03 18 00 91` | add x3,x0,#0x6 | `FALL_THROUGH`
<a id="insn-00beaea4"></a> `00beaea4` | `96 00 00 94` | bl 0x00beb0fc | `UNCONDITIONAL_CALL`
<a id="insn-00beaea8"></a> `00beaea8` | `8d 00 00 14` | b 0x00beb0dc | `UNCONDITIONAL_JUMP`
<a id="insn-00beaeac"></a> `00beaeac` | `09 04 40 79` | ldrh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaeb0"></a> `00beaeb0` | `08 00 40 79` | ldrh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaeb4"></a> `00beaeb4` | `2a e0 5f 78` | ldurh w10,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beaeb8"></a> `00beaeb8` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beaebc"></a> `00beaebc` | `62 05 00 54` | b.cs 0x00beaf68 | `CONDITIONAL_JUMP`
<a id="insn-00beaec0"></a> `00beaec0` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00beaec4"></a> `00beaec4` | `a2 0f 00 54` | b.cs 0x00beb0b8 | `CONDITIONAL_JUMP`
<a id="insn-00beaec8"></a> `00beaec8` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beaecc"></a> `00beaecc` | `81 00 00 14` | b 0x00beb0d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beaed0"></a> `00beaed0` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00beaed4"></a> `00beaed4` | `08 00 40 79` | ldrh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaed8"></a> `00beaed8` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beaedc"></a> `00beaedc` | `4c 2d 40 78` | ldrh w12,[x10, #0x2]! | `FALL_THROUGH`
<a id="insn-00beaee0"></a> `00beaee0` | `69 4d 40 78` | ldrh w9,[x11, #0x4]! | `FALL_THROUGH`
<a id="insn-00beaee4"></a> `00beaee4` | `9f 01 08 6b` | cmp w12,w8 | `FALL_THROUGH`
<a id="insn-00beaee8"></a> `00beaee8` | `62 05 00 54` | b.cs 0x00beaf94 | `CONDITIONAL_JUMP`
<a id="insn-00beaeec"></a> `00beaeec` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00beaef0"></a> `00beaef0` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beaef4"></a> `00beaef4` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beaef8"></a> `00beaef8` | `e3 05 00 54` | b.cc 0x00beafb4 | `CONDITIONAL_JUMP`
<a id="insn-00beaefc"></a> `00beaefc` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beaf00"></a> `00beaf00` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00beaf04"></a> `00beaf04` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beaf08"></a> `00beaf08` | `0c 00 00 79` | strh w12,[x0] | `FALL_THROUGH`
<a id="insn-00beaf0c"></a> `00beaf0c` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaf10"></a> `00beaf10` | `23 05 00 54` | b.cc 0x00beafb4 | `CONDITIONAL_JUMP`
<a id="insn-00beaf14"></a> `00beaf14` | `2a 00 00 14` | b 0x00beafbc | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf18"></a> `00beaf18` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00beaf1c"></a> `00beaf1c` | `0b 00 40 79` | ldrh w11,[x0] | `FALL_THROUGH`
<a id="insn-00beaf20"></a> `00beaf20` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00beaf24"></a> `00beaf24` | `0a 2d 40 78` | ldrh w10,[x8, #0x2]! | `FALL_THROUGH`
<a id="insn-00beaf28"></a> `00beaf28` | `2c 4d 40 78` | ldrh w12,[x9, #0x4]! | `FALL_THROUGH`
<a id="insn-00beaf2c"></a> `00beaf2c` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00beaf30"></a> `00beaf30` | `62 08 00 54` | b.cs 0x00beb03c | `CONDITIONAL_JUMP`
<a id="insn-00beaf34"></a> `00beaf34` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00beaf38"></a> `00beaf38` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beaf3c"></a> `00beaf3c` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00beaf40"></a> `00beaf40` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00beaf44"></a> `00beaf44` | `e3 08 00 54` | b.cc 0x00beb060 | `CONDITIONAL_JUMP`
<a id="insn-00beaf48"></a> `00beaf48` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beaf4c"></a> `00beaf4c` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00beaf50"></a> `00beaf50` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00beaf54"></a> `00beaf54` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00beaf58"></a> `00beaf58` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beaf5c"></a> `00beaf5c` | `0b 04 00 79` | strh w11,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaf60"></a> `00beaf60` | `03 08 00 54` | b.cc 0x00beb060 | `CONDITIONAL_JUMP`
<a id="insn-00beaf64"></a> `00beaf64` | `43 00 00 14` | b 0x00beb070 | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf68"></a> `00beaf68` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00beaf6c"></a> `00beaf6c` | `82 0b 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beaf70"></a> `00beaf70` | `0a 04 00 79` | strh w10,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaf74"></a> `00beaf74` | `29 e0 1f 78` | sturh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beaf78"></a> `00beaf78` | `09 04 40 79` | ldrh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaf7c"></a> `00beaf7c` | `08 00 40 79` | ldrh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaf80"></a> `00beaf80` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beaf84"></a> `00beaf84` | `c2 0a 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beaf88"></a> `00beaf88` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beaf8c"></a> `00beaf8c` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaf90"></a> `00beaf90` | `53 00 00 14` | b 0x00beb0dc | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf94"></a> `00beaf94` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00beaf98"></a> `00beaf98` | `22 01 00 54` | b.cs 0x00beafbc | `CONDITIONAL_JUMP`
<a id="insn-00beaf9c"></a> `00beaf9c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beafa0"></a> `00beafa0` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beafa4"></a> `00beafa4` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00beafa8"></a> `00beafa8` | `49 01 00 79` | strh w9,[x10] | `FALL_THROUGH`
<a id="insn-00beafac"></a> `00beafac` | `6c 01 00 79` | strh w12,[x11] | `FALL_THROUGH`
<a id="insn-00beafb0"></a> `00beafb0` | `62 00 00 54` | b.cs 0x00beafbc | `CONDITIONAL_JUMP`
<a id="insn-00beafb4"></a> `00beafb4` | `a9 01 00 79` | strh w9,[x13] | `FALL_THROUGH`
<a id="insn-00beafb8"></a> `00beafb8` | `c8 01 00 79` | strh w8,[x14] | `FALL_THROUGH`
<a id="insn-00beafbc"></a> `00beafbc` | `08 18 00 91` | add x8,x0,#0x6 | `FALL_THROUGH`
<a id="insn-00beafc0"></a> `00beafc0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beafc4"></a> `00beafc4` | `c0 08 00 54` | b.eq 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beafc8"></a> `00beafc8` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00beafcc"></a> `00beafcc` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00beafd0"></a> `00beafd0` | `0c 00 00 14` | b 0x00beb000 | `UNCONDITIONAL_JUMP`
<a id="insn-00beafd4"></a> `00beafd4` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beafd8"></a> `00beafd8` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00beafdc"></a> `00beafdc` | `6c 01 00 79` | strh w12,[x11] | `FALL_THROUGH`
<a id="insn-00beafe0"></a> `00beafe0` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00beafe4"></a> `00beafe4` | `40 08 00 54` | b.eq 0x00beb0ec | `CONDITIONAL_JUMP`
<a id="insn-00beafe8"></a> `00beafe8` | `0c 09 00 91` | add x12,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beafec"></a> `00beafec` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00beaff0"></a> `00beaff0` | `4a 09 00 91` | add x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00beaff4"></a> `00beaff4` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00beaff8"></a> `00beaff8` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00beaffc"></a> `00beaffc` | `00 07 00 54` | b.eq 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beb000"></a> `00beb000` | `0c 01 40 79` | ldrh w12,[x8] | `FALL_THROUGH`
<a id="insn-00beb004"></a> `00beb004` | `6b 01 40 79` | ldrh w11,[x11] | `FALL_THROUGH`
<a id="insn-00beb008"></a> `00beb008` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beb00c"></a> `00beb00c` | `e2 fe ff 54` | b.cs 0x00beafe8 | `CONDITIONAL_JUMP`
<a id="insn-00beb010"></a> `00beb010` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00beb014"></a> `00beb014` | `cd 09 00 f1` | subs x13,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00beb018"></a> `00beb018` | `0b 68 2e 78` | strh w11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00beb01c"></a> `00beb01c` | `c0 fd ff 54` | b.eq 0x00beafd4 | `CONDITIONAL_JUMP`
<a id="insn-00beb020"></a> `00beb020` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00beb024"></a> `00beb024` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00beb028"></a> `00beb028` | `6b c1 5f 78` | ldurh w11,[x11, #-0x4] | `FALL_THROUGH`
<a id="insn-00beb02c"></a> `00beb02c` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beb030"></a> `00beb030` | `23 ff ff 54` | b.cc 0x00beb014 | `CONDITIONAL_JUMP`
<a id="insn-00beb034"></a> `00beb034` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00beb038"></a> `00beb038` | `e8 ff ff 17` | b 0x00beafd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beb03c"></a> `00beb03c` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00beb040"></a> `00beb040` | `82 01 00 54` | b.cs 0x00beb070 | `CONDITIONAL_JUMP`
<a id="insn-00beb044"></a> `00beb044` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beb048"></a> `00beb048` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beb04c"></a> `00beb04c` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00beb050"></a> `00beb050` | `e2 03 0a 2a` | mov w2,w10 | `FALL_THROUGH`
<a id="insn-00beb054"></a> `00beb054` | `0c 01 00 79` | strh w12,[x8] | `FALL_THROUGH`
<a id="insn-00beb058"></a> `00beb058` | `2a 01 00 79` | strh w10,[x9] | `FALL_THROUGH`
<a id="insn-00beb05c"></a> `00beb05c` | `c2 00 00 54` | b.cs 0x00beb074 | `CONDITIONAL_JUMP`
<a id="insn-00beb060"></a> `00beb060` | `ea 03 02 2a` | mov w10,w2 | `FALL_THROUGH`
<a id="insn-00beb064"></a> `00beb064` | `ac 01 00 79` | strh w12,[x13] | `FALL_THROUGH`
<a id="insn-00beb068"></a> `00beb068` | `cb 01 00 79` | strh w11,[x14] | `FALL_THROUGH`
<a id="insn-00beb06c"></a> `00beb06c` | `02 00 00 14` | b 0x00beb074 | `UNCONDITIONAL_JUMP`
<a id="insn-00beb070"></a> `00beb070` | `ea 03 0c 2a` | mov w10,w12 | `FALL_THROUGH`
<a id="insn-00beb074"></a> `00beb074` | `2b e0 5f 78` | ldurh w11,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beb078"></a> `00beb078` | `7f 01 0a 6b` | cmp w11,w10 | `FALL_THROUGH`
<a id="insn-00beb07c"></a> `00beb07c` | `02 03 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beb080"></a> `00beb080` | `2b 01 00 79` | strh w11,[x9] | `FALL_THROUGH`
<a id="insn-00beb084"></a> `00beb084` | `2a e0 1f 78` | sturh w10,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beb088"></a> `00beb088` | `29 01 40 79` | ldrh w9,[x9] | `FALL_THROUGH`
<a id="insn-00beb08c"></a> `00beb08c` | `08 01 40 79` | ldrh w8,[x8] | `FALL_THROUGH`
<a id="insn-00beb090"></a> `00beb090` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beb094"></a> `00beb094` | `42 02 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beb098"></a> `00beb098` | `0a 00 40 79` | ldrh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beb09c"></a> `00beb09c` | `09 04 00 79` | strh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beb0a0"></a> `00beb0a0` | `08 08 00 79` | strh w8,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00beb0a4"></a> `00beb0a4` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00beb0a8"></a> `00beb0a8` | `a2 01 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beb0ac"></a> `00beb0ac` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb0b0"></a> `00beb0b0` | `0a 04 00 79` | strh w10,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beb0b4"></a> `00beb0b4` | `0a 00 00 14` | b 0x00beb0dc | `UNCONDITIONAL_JUMP`
<a id="insn-00beb0b8"></a> `00beb0b8` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb0bc"></a> `00beb0bc` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beb0c0"></a> `00beb0c0` | `29 e0 5f 78` | ldurh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beb0c4"></a> `00beb0c4` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beb0c8"></a> `00beb0c8` | `a2 00 00 54` | b.cs 0x00beb0dc | `CONDITIONAL_JUMP`
<a id="insn-00beb0cc"></a> `00beb0cc` | `09 04 00 79` | strh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beb0d0"></a> `00beb0d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beb0d4"></a> `00beb0d4` | `28 e0 1f 78` | sturh w8,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beb0d8"></a> `00beb0d8` | `02 00 00 14` | b 0x00beb0e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beb0dc"></a> `00beb0dc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beb0e0"></a> `00beb0e0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00beb0e4"></a> `00beb0e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00beb0e8"></a> `00beb0e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beb0ec"></a> `00beb0ec` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beb0f0"></a> `00beb0f0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beb0f4"></a> `00beb0f4` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00beb0f8"></a> `00beb0f8` | `fa ff ff 17` | b 0x00beb0e0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beae3c`](#insn-00beae3c) 範囲 `[['00beae3c', '00beae57']]`
  - `CONDITIONAL_JUMP` [`00beae54`](#insn-00beae54) → [`00beae7c`](#insn-00beae7c)
  - `FALL_THROUGH` [`00beae54`](#insn-00beae54) → [`00beae58`](#insn-00beae58)
- ブロック [`00beae58`](#insn-00beae58) 範囲 `[['00beae58', '00beae5b']]`
  - `CONDITIONAL_JUMP` [`00beae58`](#insn-00beae58) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beae58`](#insn-00beae58) → [`00beae5c`](#insn-00beae5c)
- ブロック [`00beae5c`](#insn-00beae5c) 範囲 `[['00beae5c', '00beae63']]`
  - `CONDITIONAL_JUMP` [`00beae60`](#insn-00beae60) → [`00beaed0`](#insn-00beaed0)
  - `FALL_THROUGH` [`00beae60`](#insn-00beae60) → [`00beae64`](#insn-00beae64)
- ブロック [`00beae64`](#insn-00beae64) 範囲 `[['00beae64', '00beae73']]`
  - `CONDITIONAL_JUMP` [`00beae70`](#insn-00beae70) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beae70`](#insn-00beae70) → [`00beae74`](#insn-00beae74)
- ブロック [`00beae74`](#insn-00beae74) 範囲 `[['00beae74', '00beae7b']]`
  - `UNCONDITIONAL_JUMP` [`00beae78`](#insn-00beae78) → [`00beb0d0`](#insn-00beb0d0)
- ブロック [`00beae7c`](#insn-00beae7c) 範囲 `[['00beae7c', '00beae83']]`
  - `CONDITIONAL_JUMP` [`00beae80`](#insn-00beae80) → [`00beaeac`](#insn-00beaeac)
  - `FALL_THROUGH` [`00beae80`](#insn-00beae80) → [`00beae84`](#insn-00beae84)
- ブロック [`00beae84`](#insn-00beae84) 範囲 `[['00beae84', '00beae8b']]`
  - `CONDITIONAL_JUMP` [`00beae88`](#insn-00beae88) → [`00beaf18`](#insn-00beaf18)
  - `FALL_THROUGH` [`00beae88`](#insn-00beae88) → [`00beae8c`](#insn-00beae8c)
- ブロック [`00beae8c`](#insn-00beae8c) 範囲 `[['00beae8c', '00beae93']]`
  - `CONDITIONAL_JUMP` [`00beae90`](#insn-00beae90) → [`00beaed0`](#insn-00beaed0)
  - `FALL_THROUGH` [`00beae90`](#insn-00beae90) → [`00beae94`](#insn-00beae94)
- ブロック [`00beae94`](#insn-00beae94) 範囲 `[['00beae94', '00beaeab']]`
  - `UNCONDITIONAL_JUMP` [`00beaea8`](#insn-00beaea8) → [`00beb0dc`](#insn-00beb0dc)
- ブロック [`00beaeac`](#insn-00beaeac) 範囲 `[['00beaeac', '00beaebf']]`
  - `CONDITIONAL_JUMP` [`00beaebc`](#insn-00beaebc) → [`00beaf68`](#insn-00beaf68)
  - `FALL_THROUGH` [`00beaebc`](#insn-00beaebc) → [`00beaec0`](#insn-00beaec0)
- ブロック [`00beaec0`](#insn-00beaec0) 範囲 `[['00beaec0', '00beaec7']]`
  - `CONDITIONAL_JUMP` [`00beaec4`](#insn-00beaec4) → [`00beb0b8`](#insn-00beb0b8)
  - `FALL_THROUGH` [`00beaec4`](#insn-00beaec4) → [`00beaec8`](#insn-00beaec8)
- ブロック [`00beaec8`](#insn-00beaec8) 範囲 `[['00beaec8', '00beaecf']]`
  - `UNCONDITIONAL_JUMP` [`00beaecc`](#insn-00beaecc) → [`00beb0d0`](#insn-00beb0d0)
- ブロック [`00beaed0`](#insn-00beaed0) 範囲 `[['00beaed0', '00beaeeb']]`
  - `CONDITIONAL_JUMP` [`00beaee8`](#insn-00beaee8) → [`00beaf94`](#insn-00beaf94)
  - `FALL_THROUGH` [`00beaee8`](#insn-00beaee8) → [`00beaeec`](#insn-00beaeec)
- ブロック [`00beaeec`](#insn-00beaeec) 範囲 `[['00beaeec', '00beaefb']]`
  - `CONDITIONAL_JUMP` [`00beaef8`](#insn-00beaef8) → [`00beafb4`](#insn-00beafb4)
  - `FALL_THROUGH` [`00beaef8`](#insn-00beaef8) → [`00beaefc`](#insn-00beaefc)
- ブロック [`00beaefc`](#insn-00beaefc) 範囲 `[['00beaefc', '00beaf13']]`
  - `CONDITIONAL_JUMP` [`00beaf10`](#insn-00beaf10) → [`00beafb4`](#insn-00beafb4)
  - `FALL_THROUGH` [`00beaf10`](#insn-00beaf10) → [`00beaf14`](#insn-00beaf14)
- ブロック [`00beaf14`](#insn-00beaf14) 範囲 `[['00beaf14', '00beaf17']]`
  - `UNCONDITIONAL_JUMP` [`00beaf14`](#insn-00beaf14) → [`00beafbc`](#insn-00beafbc)
- ブロック [`00beaf18`](#insn-00beaf18) 範囲 `[['00beaf18', '00beaf33']]`
  - `CONDITIONAL_JUMP` [`00beaf30`](#insn-00beaf30) → [`00beb03c`](#insn-00beb03c)
  - `FALL_THROUGH` [`00beaf30`](#insn-00beaf30) → [`00beaf34`](#insn-00beaf34)
- ブロック [`00beaf34`](#insn-00beaf34) 範囲 `[['00beaf34', '00beaf47']]`
  - `CONDITIONAL_JUMP` [`00beaf44`](#insn-00beaf44) → [`00beb060`](#insn-00beb060)
  - `FALL_THROUGH` [`00beaf44`](#insn-00beaf44) → [`00beaf48`](#insn-00beaf48)
- ブロック [`00beaf48`](#insn-00beaf48) 範囲 `[['00beaf48', '00beaf63']]`
  - `CONDITIONAL_JUMP` [`00beaf60`](#insn-00beaf60) → [`00beb060`](#insn-00beb060)
  - `FALL_THROUGH` [`00beaf60`](#insn-00beaf60) → [`00beaf64`](#insn-00beaf64)
- ブロック [`00beaf64`](#insn-00beaf64) 範囲 `[['00beaf64', '00beaf67']]`
  - `UNCONDITIONAL_JUMP` [`00beaf64`](#insn-00beaf64) → [`00beb070`](#insn-00beb070)
- ブロック [`00beaf68`](#insn-00beaf68) 範囲 `[['00beaf68', '00beaf6f']]`
  - `CONDITIONAL_JUMP` [`00beaf6c`](#insn-00beaf6c) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beaf6c`](#insn-00beaf6c) → [`00beaf70`](#insn-00beaf70)
- ブロック [`00beaf70`](#insn-00beaf70) 範囲 `[['00beaf70', '00beaf87']]`
  - `CONDITIONAL_JUMP` [`00beaf84`](#insn-00beaf84) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beaf84`](#insn-00beaf84) → [`00beaf88`](#insn-00beaf88)
- ブロック [`00beaf88`](#insn-00beaf88) 範囲 `[['00beaf88', '00beaf93']]`
  - `UNCONDITIONAL_JUMP` [`00beaf90`](#insn-00beaf90) → [`00beb0dc`](#insn-00beb0dc)
- ブロック [`00beaf94`](#insn-00beaf94) 範囲 `[['00beaf94', '00beaf9b']]`
  - `CONDITIONAL_JUMP` [`00beaf98`](#insn-00beaf98) → [`00beafbc`](#insn-00beafbc)
  - `FALL_THROUGH` [`00beaf98`](#insn-00beaf98) → [`00beaf9c`](#insn-00beaf9c)
- ブロック [`00beaf9c`](#insn-00beaf9c) 範囲 `[['00beaf9c', '00beafb3']]`
  - `CONDITIONAL_JUMP` [`00beafb0`](#insn-00beafb0) → [`00beafbc`](#insn-00beafbc)
  - `FALL_THROUGH` [`00beafb0`](#insn-00beafb0) → [`00beafb4`](#insn-00beafb4)
- ブロック [`00beafb4`](#insn-00beafb4) 範囲 `[['00beafb4', '00beafbb']]`
  - `FALL_THROUGH` [`00beafb8`](#insn-00beafb8) → [`00beafbc`](#insn-00beafbc)
- ブロック [`00beafbc`](#insn-00beafbc) 範囲 `[['00beafbc', '00beafc7']]`
  - `CONDITIONAL_JUMP` [`00beafc4`](#insn-00beafc4) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beafc4`](#insn-00beafc4) → [`00beafc8`](#insn-00beafc8)
- ブロック [`00beafc8`](#insn-00beafc8) 範囲 `[['00beafc8', '00beafd3']]`
  - `UNCONDITIONAL_JUMP` [`00beafd0`](#insn-00beafd0) → [`00beb000`](#insn-00beb000)
- ブロック [`00beafd4`](#insn-00beafd4) 範囲 `[['00beafd4', '00beafd7']]`
  - `FALL_THROUGH` [`00beafd4`](#insn-00beafd4) → [`00beafd8`](#insn-00beafd8)
- ブロック [`00beafd8`](#insn-00beafd8) 範囲 `[['00beafd8', '00beafe7']]`
  - `CONDITIONAL_JUMP` [`00beafe4`](#insn-00beafe4) → [`00beb0ec`](#insn-00beb0ec)
  - `FALL_THROUGH` [`00beafe4`](#insn-00beafe4) → [`00beafe8`](#insn-00beafe8)
- ブロック [`00beafe8`](#insn-00beafe8) 範囲 `[['00beafe8', '00beafff']]`
  - `CONDITIONAL_JUMP` [`00beaffc`](#insn-00beaffc) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beaffc`](#insn-00beaffc) → [`00beb000`](#insn-00beb000)
- ブロック [`00beb000`](#insn-00beb000) 範囲 `[['00beb000', '00beb00f']]`
  - `CONDITIONAL_JUMP` [`00beb00c`](#insn-00beb00c) → [`00beafe8`](#insn-00beafe8)
  - `FALL_THROUGH` [`00beb00c`](#insn-00beb00c) → [`00beb010`](#insn-00beb010)
- ブロック [`00beb010`](#insn-00beb010) 範囲 `[['00beb010', '00beb013']]`
  - `FALL_THROUGH` [`00beb010`](#insn-00beb010) → [`00beb014`](#insn-00beb014)
- ブロック [`00beb014`](#insn-00beb014) 範囲 `[['00beb014', '00beb01f']]`
  - `CONDITIONAL_JUMP` [`00beb01c`](#insn-00beb01c) → [`00beafd4`](#insn-00beafd4)
  - `FALL_THROUGH` [`00beb01c`](#insn-00beb01c) → [`00beb020`](#insn-00beb020)
- ブロック [`00beb020`](#insn-00beb020) 範囲 `[['00beb020', '00beb033']]`
  - `CONDITIONAL_JUMP` [`00beb030`](#insn-00beb030) → [`00beb014`](#insn-00beb014)
  - `FALL_THROUGH` [`00beb030`](#insn-00beb030) → [`00beb034`](#insn-00beb034)
- ブロック [`00beb034`](#insn-00beb034) 範囲 `[['00beb034', '00beb03b']]`
  - `UNCONDITIONAL_JUMP` [`00beb038`](#insn-00beb038) → [`00beafd8`](#insn-00beafd8)
- ブロック [`00beb03c`](#insn-00beb03c) 範囲 `[['00beb03c', '00beb043']]`
  - `CONDITIONAL_JUMP` [`00beb040`](#insn-00beb040) → [`00beb070`](#insn-00beb070)
  - `FALL_THROUGH` [`00beb040`](#insn-00beb040) → [`00beb044`](#insn-00beb044)
- ブロック [`00beb044`](#insn-00beb044) 範囲 `[['00beb044', '00beb05f']]`
  - `CONDITIONAL_JUMP` [`00beb05c`](#insn-00beb05c) → [`00beb074`](#insn-00beb074)
  - `FALL_THROUGH` [`00beb05c`](#insn-00beb05c) → [`00beb060`](#insn-00beb060)
- ブロック [`00beb060`](#insn-00beb060) 範囲 `[['00beb060', '00beb06f']]`
  - `UNCONDITIONAL_JUMP` [`00beb06c`](#insn-00beb06c) → [`00beb074`](#insn-00beb074)
- ブロック [`00beb070`](#insn-00beb070) 範囲 `[['00beb070', '00beb073']]`
  - `FALL_THROUGH` [`00beb070`](#insn-00beb070) → [`00beb074`](#insn-00beb074)
- ブロック [`00beb074`](#insn-00beb074) 範囲 `[['00beb074', '00beb07f']]`
  - `CONDITIONAL_JUMP` [`00beb07c`](#insn-00beb07c) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beb07c`](#insn-00beb07c) → [`00beb080`](#insn-00beb080)
- ブロック [`00beb080`](#insn-00beb080) 範囲 `[['00beb080', '00beb097']]`
  - `CONDITIONAL_JUMP` [`00beb094`](#insn-00beb094) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beb094`](#insn-00beb094) → [`00beb098`](#insn-00beb098)
- ブロック [`00beb098`](#insn-00beb098) 範囲 `[['00beb098', '00beb0ab']]`
  - `CONDITIONAL_JUMP` [`00beb0a8`](#insn-00beb0a8) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beb0a8`](#insn-00beb0a8) → [`00beb0ac`](#insn-00beb0ac)
- ブロック [`00beb0ac`](#insn-00beb0ac) 範囲 `[['00beb0ac', '00beb0b7']]`
  - `UNCONDITIONAL_JUMP` [`00beb0b4`](#insn-00beb0b4) → [`00beb0dc`](#insn-00beb0dc)
- ブロック [`00beb0b8`](#insn-00beb0b8) 範囲 `[['00beb0b8', '00beb0cb']]`
  - `CONDITIONAL_JUMP` [`00beb0c8`](#insn-00beb0c8) → [`00beb0dc`](#insn-00beb0dc)
  - `FALL_THROUGH` [`00beb0c8`](#insn-00beb0c8) → [`00beb0cc`](#insn-00beb0cc)
- ブロック [`00beb0cc`](#insn-00beb0cc) 範囲 `[['00beb0cc', '00beb0cf']]`
  - `FALL_THROUGH` [`00beb0cc`](#insn-00beb0cc) → [`00beb0d0`](#insn-00beb0d0)
- ブロック [`00beb0d0`](#insn-00beb0d0) 範囲 `[['00beb0d0', '00beb0db']]`
  - `UNCONDITIONAL_JUMP` [`00beb0d8`](#insn-00beb0d8) → [`00beb0e0`](#insn-00beb0e0)
- ブロック [`00beb0dc`](#insn-00beb0dc) 範囲 `[['00beb0dc', '00beb0df']]`
  - `FALL_THROUGH` [`00beb0dc`](#insn-00beb0dc) → [`00beb0e0`](#insn-00beb0e0)
- ブロック [`00beb0e0`](#insn-00beb0e0) 範囲 `[['00beb0e0', '00beb0eb']]`
- ブロック [`00beb0ec`](#insn-00beb0ec) 範囲 `[['00beb0ec', '00beb0fb']]`
  - `UNCONDITIONAL_JUMP` [`00beb0f8`](#insn-00beb0f8) → [`00beb0e0`](#insn-00beb0e0)

## 命令位置別の参照

- [`00beae40`](#insn-00beae40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae54`](#insn-00beae54) → [`00beae7c`](#insn-00beae7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae58`](#insn-00beae58) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae60`](#insn-00beae60) → [`00beaed0`](#insn-00beaed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae70`](#insn-00beae70) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae78`](#insn-00beae78) → [`00beb0d0`](#insn-00beb0d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae80`](#insn-00beae80) → [`00beaeac`](#insn-00beaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae88`](#insn-00beae88) → [`00beaf18`](#insn-00beaf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae90`](#insn-00beae90) → [`00beaed0`](#insn-00beaed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaea4`](#insn-00beaea4) → [`00beb0fc`](../00beb/00beb0fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00beb0fc` · 推定シンボル `None` · 推定型 `None`
- [`00beaea8`](#insn-00beaea8) → [`00beb0dc`](#insn-00beb0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaebc`](#insn-00beaebc) → [`00beaf68`](#insn-00beaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaec4`](#insn-00beaec4) → [`00beb0b8`](#insn-00beb0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaecc`](#insn-00beaecc) → [`00beb0d0`](#insn-00beb0d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaee8`](#insn-00beaee8) → [`00beaf94`](#insn-00beaf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaef8`](#insn-00beaef8) → [`00beafb4`](#insn-00beafb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf10`](#insn-00beaf10) → [`00beafb4`](#insn-00beafb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf14`](#insn-00beaf14) → [`00beafbc`](#insn-00beafbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf30`](#insn-00beaf30) → [`00beb03c`](#insn-00beb03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf44`](#insn-00beaf44) → [`00beb060`](#insn-00beb060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf60`](#insn-00beaf60) → [`00beb060`](#insn-00beb060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf64`](#insn-00beaf64) → [`00beb070`](#insn-00beb070) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf6c`](#insn-00beaf6c) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf84`](#insn-00beaf84) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf90`](#insn-00beaf90) → [`00beb0dc`](#insn-00beb0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf98`](#insn-00beaf98) → [`00beafbc`](#insn-00beafbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafb0`](#insn-00beafb0) → [`00beafbc`](#insn-00beafbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafc4`](#insn-00beafc4) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafd0`](#insn-00beafd0) → [`00beb000`](#insn-00beb000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafe4`](#insn-00beafe4) → [`00beb0ec`](#insn-00beb0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaffc`](#insn-00beaffc) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb00c`](#insn-00beb00c) → [`00beafe8`](#insn-00beafe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb01c`](#insn-00beb01c) → [`00beafd4`](#insn-00beafd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb030`](#insn-00beb030) → [`00beb014`](#insn-00beb014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb038`](#insn-00beb038) → [`00beafd8`](#insn-00beafd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb040`](#insn-00beb040) → [`00beb070`](#insn-00beb070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb05c`](#insn-00beb05c) → [`00beb074`](#insn-00beb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb06c`](#insn-00beb06c) → [`00beb074`](#insn-00beb074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb07c`](#insn-00beb07c) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb094`](#insn-00beb094) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0a8`](#insn-00beb0a8) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0b4`](#insn-00beb0b4) → [`00beb0dc`](#insn-00beb0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0c8`](#insn-00beb0c8) → [`00beb0dc`](#insn-00beb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0d8`](#insn-00beb0d8) → [`00beb0e0`](#insn-00beb0e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0e0`](#insn-00beb0e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb0f8`](#insn-00beb0f8) → [`00beb0e0`](#insn-00beb0e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beae40`](#insn-00beae40)

~~~json
{
  "source": "00beae40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae54`](#insn-00beae54)

~~~json
{
  "source": "00beae54",
  "target": "00beae7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae58`](#insn-00beae58)

~~~json
{
  "source": "00beae58",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae60`](#insn-00beae60)

~~~json
{
  "source": "00beae60",
  "target": "00beaed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae70`](#insn-00beae70)

~~~json
{
  "source": "00beae70",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae78`](#insn-00beae78)

~~~json
{
  "source": "00beae78",
  "target": "00beb0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae80`](#insn-00beae80)

~~~json
{
  "source": "00beae80",
  "target": "00beaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae88`](#insn-00beae88)

~~~json
{
  "source": "00beae88",
  "target": "00beaf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae90`](#insn-00beae90)

~~~json
{
  "source": "00beae90",
  "target": "00beaed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaea4`](#insn-00beaea4)

~~~json
{
  "source": "00beaea4",
  "target": "00beb0fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beaea8`](#insn-00beaea8)

~~~json
{
  "source": "00beaea8",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaebc`](#insn-00beaebc)

~~~json
{
  "source": "00beaebc",
  "target": "00beaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaec4`](#insn-00beaec4)

~~~json
{
  "source": "00beaec4",
  "target": "00beb0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaecc`](#insn-00beaecc)

~~~json
{
  "source": "00beaecc",
  "target": "00beb0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaee8`](#insn-00beaee8)

~~~json
{
  "source": "00beaee8",
  "target": "00beaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaef8`](#insn-00beaef8)

~~~json
{
  "source": "00beaef8",
  "target": "00beafb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf10`](#insn-00beaf10)

~~~json
{
  "source": "00beaf10",
  "target": "00beafb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf14`](#insn-00beaf14)

~~~json
{
  "source": "00beaf14",
  "target": "00beafbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf30`](#insn-00beaf30)

~~~json
{
  "source": "00beaf30",
  "target": "00beb03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf44`](#insn-00beaf44)

~~~json
{
  "source": "00beaf44",
  "target": "00beb060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf60`](#insn-00beaf60)

~~~json
{
  "source": "00beaf60",
  "target": "00beb060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf64`](#insn-00beaf64)

~~~json
{
  "source": "00beaf64",
  "target": "00beb070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf6c`](#insn-00beaf6c)

~~~json
{
  "source": "00beaf6c",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf84`](#insn-00beaf84)

~~~json
{
  "source": "00beaf84",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf90`](#insn-00beaf90)

~~~json
{
  "source": "00beaf90",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf98`](#insn-00beaf98)

~~~json
{
  "source": "00beaf98",
  "target": "00beafbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafb0`](#insn-00beafb0)

~~~json
{
  "source": "00beafb0",
  "target": "00beafbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafc4`](#insn-00beafc4)

~~~json
{
  "source": "00beafc4",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafd0`](#insn-00beafd0)

~~~json
{
  "source": "00beafd0",
  "target": "00beb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafe4`](#insn-00beafe4)

~~~json
{
  "source": "00beafe4",
  "target": "00beb0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaffc`](#insn-00beaffc)

~~~json
{
  "source": "00beaffc",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb00c`](#insn-00beb00c)

~~~json
{
  "source": "00beb00c",
  "target": "00beafe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb01c`](#insn-00beb01c)

~~~json
{
  "source": "00beb01c",
  "target": "00beafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb030`](#insn-00beb030)

~~~json
{
  "source": "00beb030",
  "target": "00beb014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb038`](#insn-00beb038)

~~~json
{
  "source": "00beb038",
  "target": "00beafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb040`](#insn-00beb040)

~~~json
{
  "source": "00beb040",
  "target": "00beb070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb05c`](#insn-00beb05c)

~~~json
{
  "source": "00beb05c",
  "target": "00beb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb06c`](#insn-00beb06c)

~~~json
{
  "source": "00beb06c",
  "target": "00beb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb07c`](#insn-00beb07c)

~~~json
{
  "source": "00beb07c",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb094`](#insn-00beb094)

~~~json
{
  "source": "00beb094",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0a8`](#insn-00beb0a8)

~~~json
{
  "source": "00beb0a8",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0b4`](#insn-00beb0b4)

~~~json
{
  "source": "00beb0b4",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0c8`](#insn-00beb0c8)

~~~json
{
  "source": "00beb0c8",
  "target": "00beb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0d8`](#insn-00beb0d8)

~~~json
{
  "source": "00beb0d8",
  "target": "00beb0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0e0`](#insn-00beb0e0)

~~~json
{
  "source": "00beb0e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb0f8`](#insn-00beb0f8)

~~~json
{
  "source": "00beb0f8",
  "target": "00beb0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
