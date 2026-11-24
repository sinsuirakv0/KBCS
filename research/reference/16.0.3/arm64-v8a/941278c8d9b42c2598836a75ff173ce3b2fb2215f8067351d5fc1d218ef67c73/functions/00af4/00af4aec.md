# 00af4aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0082.md#review-953006fa3bd9b85290007d9916f0ac5a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af4aec",
  "name": "FUN_00af4aec",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97665991fb00a6c9a82e41f61f099e67c6d4ca6011c4c233a84abee899826a29",
  "source_text_sha256": "97665991fb00a6c9a82e41f61f099e67c6d4ca6011c4c233a84abee899826a29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af4aec",
        "00af4cab"
      ]
    ],
    "bytes_sha256": "a4ef11b303ad1953a2682167cd1be916f99e72a40374d19b8c87b9d93961674b",
    "instruction_count": 112,
    "instruction_bytes": 448,
    "body_bytes": 448,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f3e60](../005f3/005f3e60.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [00713760](../00713/00713760.md)
- [00714664](../00714/00714664.md)
- [00714ff0](../00714/00714ff0.md)
- [007151c0](../00715/007151c0.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 関連文字列（未確認候補）

~~~text
"NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS6_ISB_EEFbRKNS_10shared_ptrIN2fs8FileDataEEEEEE"
"ZN11aDownloader8downloadERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEiiE3$_1"
"provider_id && id_token && raw_nonce"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2258 bytes

~~~c

void FUN_00af4aec(undefined8 *param_1,int param_2,int param_3)

{
  byte *pbVar1;
  byte bVar2;
  long lVar3;
  ulong uVar4;
  long lVar5;
  undefined1 uVar6;
  undefined4 uVar7;
  long lVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  
  lVar3 = FUN_008524fc();
  if ((*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) == 0) ||
     (lVar3 = FUN_008524fc(),
     *(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) != 1)) {
    lVar3 = FUN_008524fc();
    if (*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) != 0) {
      FUN_008524fc();
      lVar3 = FUN_008524fc();
      uVar4 = FUN_005e7810(lVar3 + (long)param_2 * 0x1f0 + 0x2768);
      lVar3 = FUN_008524fc();
      if ((uVar4 & 1) == 0) {
        lVar5 = FUN_008524fc();
        pbVar1 = (byte *)("provider_id && id_token && raw_nonce" +
                         lVar3 + (long)*(int *)(lVar5 + (long)param_2 * 0xc804 +
                                                (long)param_3 * 0x3ec + 0x848c8) * 0x18 + 7);
        bVar2 = *pbVar1;
      }
      else {
        lVar8 = (long)*(int *)(lVar3 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x848c8) +
                -2;
        lVar3 = FUN_008524fc();
        lVar5 = FUN_008524fc();
        pbVar1 = (byte *)(
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS6_ISB_EEFbRKNS_10shared_ptrIN2fs8FileDataEEEEEE"
                         + lVar3 + lVar8 * 0x1e0 +
                           (long)*(int *)(lVar5 + lVar8 * 4 + 0x49934) * 0x78 + 0xa2);
        bVar2 = *pbVar1;
      }
      if ((bVar2 & 1) == 0) {
        uVar10 = *(undefined8 *)(pbVar1 + 8);
        uVar9 = *(undefined8 *)pbVar1;
        param_1[2] = *(undefined8 *)(pbVar1 + 0x10);
        param_1[1] = uVar10;
        *param_1 = uVar9;
        return;
      }
      FUN_0043be80(param_1,*(undefined8 *)(pbVar1 + 0x10),*(undefined8 *)(pbVar1 + 8));
      return;
    }
    uVar6 = 8;
    *(undefined1 *)((long)param_1 + 5) = 0;
    uVar7 = 0x656e6f4e;
  }
  else {
    uVar6 = 6;
    uVar7 = 0x8e9fe5;
  }
  *(undefined1 *)param_1 = uVar6;
  *(undefined4 *)((long)param_1 + 1) = uVar7;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af4aec"></a> `00af4aec` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00af4af0"></a> `00af4af0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4af4"></a> `00af4af4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4af8"></a> `00af4af8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af4afc"></a> `00af4afc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af4b00"></a> `00af4b00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af4b04"></a> `00af4b04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af4b08"></a> `00af4b08` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00af4b0c"></a> `00af4b0c` | `7c 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4b10"></a> `00af4b10` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4b14"></a> `00af4b14` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4b18"></a> `00af4b18` | `b7 7e 40 93` | sxtw x23,w21 | `FALL_THROUGH`
<a id="insn-00af4b1c"></a> `00af4b1c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4b20"></a> `00af4b20` | `96 7e 40 93` | sxtw x22,w20 | `FALL_THROUGH`
<a id="insn-00af4b24"></a> `00af4b24` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4b28"></a> `00af4b28` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af4b2c"></a> `00af4b2c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4b30"></a> `00af4b30` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4b34"></a> `00af4b34` | `e8 01 00 34` | cbz w8,0x00af4b70 | `CONDITIONAL_JUMP`
<a id="insn-00af4b38"></a> `00af4b38` | `71 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4b3c"></a> `00af4b3c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4b40"></a> `00af4b40` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4b44"></a> `00af4b44` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4b48"></a> `00af4b48` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4b4c"></a> `00af4b4c` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af4b50"></a> `00af4b50` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4b54"></a> `00af4b54` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4b58"></a> `00af4b58` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af4b5c"></a> `00af4b5c` | `a1 00 00 54` | b.ne 0x00af4b70 | `CONDITIONAL_JUMP`
<a id="insn-00af4b60"></a> `00af4b60` | `a9 fc 93 52` | mov w9,#0x9fe5 | `FALL_THROUGH`
<a id="insn-00af4b64"></a> `00af4b64` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00af4b68"></a> `00af4b68` | `c9 11 a0 72` | movk w9,#0x8e, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4b6c"></a> `00af4b6c` | `2e 00 00 14` | b 0x00af4c24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4b70"></a> `00af4b70` | `63 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4b74"></a> `00af4b74` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4b78"></a> `00af4b78` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4b7c"></a> `00af4b7c` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4b80"></a> `00af4b80` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4b84"></a> `00af4b84` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af4b88"></a> `00af4b88` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4b8c"></a> `00af4b8c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4b90"></a> `00af4b90` | `28 04 00 34` | cbz w8,0x00af4c14 | `CONDITIONAL_JUMP`
<a id="insn-00af4b94"></a> `00af4b94` | `5a 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4b98"></a> `00af4b98` | `59 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4b9c"></a> `00af4b9c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af4ba0"></a> `00af4ba0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af4ba4"></a> `00af4ba4` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4ba8"></a> `00af4ba8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af4bac"></a> `00af4bac` | `19 cb eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00af4bb0"></a> `00af4bb0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af4bb4"></a> `00af4bb4` | `52 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4bb8"></a> `00af4bb8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00af4bbc"></a> `00af4bbc` | `b5 03 00 37` | tbnz w21,#0x0,0x00af4c30 | `CONDITIONAL_JUMP`
<a id="insn-00af4bc0"></a> `00af4bc0` | `4f 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4bc4"></a> `00af4bc4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4bc8"></a> `00af4bc8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4bcc"></a> `00af4bcc` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4bd0"></a> `00af4bd0` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4bd4"></a> `00af4bd4` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af4bd8"></a> `00af4bd8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4bdc"></a> `00af4bdc` | `08 69 a9 b8` | ldrsw x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4be0"></a> `00af4be0` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00af4be4"></a> `00af4be4` | `08 51 29 9b` | smaddl x8,w8,w9,x20 | `FALL_THROUGH`
<a id="insn-00af4be8"></a> `00af4be8` | `08 fd 4a 91` | add x8,x8,#0x2bf, LSL #12 | `FALL_THROUGH`
<a id="insn-00af4bec"></a> `00af4bec` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00af4bf0"></a> `00af4bf0` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00af4bf4"></a> `00af4bf4` | `a9 04 00 36` | tbz w9,#0x0,0x00af4c88 | `CONDITIONAL_JUMP`
<a id="insn-00af4bf8"></a> `00af4bf8` | `02 85 40 a9` | ldp x2,x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00af4bfc"></a> `00af4bfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af4c00"></a> `00af4c00` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af4c04"></a> `00af4c04` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4c08"></a> `00af4c08` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4c0c"></a> `00af4c0c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00af4c10"></a> `00af4c10` | `9c 1c e5 17` | b 0x0043be80 | `CALL_TERMINATOR`
<a id="insn-00af4c14"></a> `00af4c14` | `c9 e9 8d 52` | mov w9,#0x6f4e | `FALL_THROUGH`
<a id="insn-00af4c18"></a> `00af4c18` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00af4c1c"></a> `00af4c1c` | `7f 16 00 39` | strb wzr,[x19, #0x5] | `FALL_THROUGH`
<a id="insn-00af4c20"></a> `00af4c20` | `c9 ad ac 72` | movk w9,#0x656e, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4c24"></a> `00af4c24` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00af4c28"></a> `00af4c28` | `69 12 00 b8` | stur w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00af4c2c"></a> `00af4c2c` | `1b 00 00 14` | b 0x00af4c98 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4c30"></a> `00af4c30` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4c34"></a> `00af4c34` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4c38"></a> `00af4c38` | `e8 52 28 9b` | smaddl x8,w23,w8,x20 | `FALL_THROUGH`
<a id="insn-00af4c3c"></a> `00af4c3c` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4c40"></a> `00af4c40` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af4c44"></a> `00af4c44` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4c48"></a> `00af4c48` | `08 69 a9 b8` | ldrsw x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4c4c"></a> `00af4c4c` | `14 09 00 d1` | sub x20,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00af4c50"></a> `00af4c50` | `2b 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4c54"></a> `00af4c54` | `08 3c 80 52` | mov w8,#0x1e0 | `FALL_THROUGH`
<a id="insn-00af4c58"></a> `00af4c58` | `95 02 08 9b` | madd x21,x20,x8,x0 | `FALL_THROUGH`
<a id="insn-00af4c5c"></a> `00af4c5c` | `28 76 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4c60"></a> `00af4c60` | `08 08 14 8b` | add x8,x0,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00af4c64"></a> `00af4c64` | `89 26 93 52` | mov w9,#0x9934 | `FALL_THROUGH`
<a id="insn-00af4c68"></a> `00af4c68` | `89 00 a0 72` | movk w9,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4c6c"></a> `00af4c6c` | `08 69 a9 b8` | ldrsw x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4c70"></a> `00af4c70` | `09 0f 80 52` | mov w9,#0x78 | `FALL_THROUGH`
<a id="insn-00af4c74"></a> `00af4c74` | `08 55 29 9b` | smaddl x8,w8,w9,x21 | `FALL_THROUGH`
<a id="insn-00af4c78"></a> `00af4c78` | `08 11 4b 91` | add x8,x8,#0x2c4, LSL #12 | `FALL_THROUGH`
<a id="insn-00af4c7c"></a> `00af4c7c` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-00af4c80"></a> `00af4c80` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00af4c84"></a> `00af4c84` | `a9 fb 07 37` | tbnz w9,#0x0,0x00af4bf8 | `CONDITIONAL_JUMP`
<a id="insn-00af4c88"></a> `00af4c88` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af4c8c"></a> `00af4c8c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00af4c90"></a> `00af4c90` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00af4c94"></a> `00af4c94` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00af4c98"></a> `00af4c98` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af4c9c"></a> `00af4c9c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4ca0"></a> `00af4ca0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4ca4"></a> `00af4ca4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00af4ca8"></a> `00af4ca8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af4aec`](#insn-00af4aec) 範囲 `[['00af4aec', '00af4b37']]`
  - `CONDITIONAL_JUMP` [`00af4b34`](#insn-00af4b34) → [`00af4b70`](#insn-00af4b70)
  - `FALL_THROUGH` [`00af4b34`](#insn-00af4b34) → [`00af4b38`](#insn-00af4b38)
- ブロック [`00af4b38`](#insn-00af4b38) 範囲 `[['00af4b38', '00af4b5f']]`
  - `CONDITIONAL_JUMP` [`00af4b5c`](#insn-00af4b5c) → [`00af4b70`](#insn-00af4b70)
  - `FALL_THROUGH` [`00af4b5c`](#insn-00af4b5c) → [`00af4b60`](#insn-00af4b60)
- ブロック [`00af4b60`](#insn-00af4b60) 範囲 `[['00af4b60', '00af4b6f']]`
  - `UNCONDITIONAL_JUMP` [`00af4b6c`](#insn-00af4b6c) → [`00af4c24`](#insn-00af4c24)
- ブロック [`00af4b70`](#insn-00af4b70) 範囲 `[['00af4b70', '00af4b93']]`
  - `CONDITIONAL_JUMP` [`00af4b90`](#insn-00af4b90) → [`00af4c14`](#insn-00af4c14)
  - `FALL_THROUGH` [`00af4b90`](#insn-00af4b90) → [`00af4b94`](#insn-00af4b94)
- ブロック [`00af4b94`](#insn-00af4b94) 範囲 `[['00af4b94', '00af4bbf']]`
  - `CONDITIONAL_JUMP` [`00af4bbc`](#insn-00af4bbc) → [`00af4c30`](#insn-00af4c30)
  - `FALL_THROUGH` [`00af4bbc`](#insn-00af4bbc) → [`00af4bc0`](#insn-00af4bc0)
- ブロック [`00af4bc0`](#insn-00af4bc0) 範囲 `[['00af4bc0', '00af4bf7']]`
  - `CONDITIONAL_JUMP` [`00af4bf4`](#insn-00af4bf4) → [`00af4c88`](#insn-00af4c88)
  - `FALL_THROUGH` [`00af4bf4`](#insn-00af4bf4) → [`00af4bf8`](#insn-00af4bf8)
- ブロック [`00af4bf8`](#insn-00af4bf8) 範囲 `[['00af4bf8', '00af4c13']]`
- ブロック [`00af4c14`](#insn-00af4c14) 範囲 `[['00af4c14', '00af4c23']]`
  - `FALL_THROUGH` [`00af4c20`](#insn-00af4c20) → [`00af4c24`](#insn-00af4c24)
- ブロック [`00af4c24`](#insn-00af4c24) 範囲 `[['00af4c24', '00af4c2f']]`
  - `UNCONDITIONAL_JUMP` [`00af4c2c`](#insn-00af4c2c) → [`00af4c98`](#insn-00af4c98)
- ブロック [`00af4c30`](#insn-00af4c30) 範囲 `[['00af4c30', '00af4c87']]`
  - `CONDITIONAL_JUMP` [`00af4c84`](#insn-00af4c84) → [`00af4bf8`](#insn-00af4bf8)
  - `FALL_THROUGH` [`00af4c84`](#insn-00af4c84) → [`00af4c88`](#insn-00af4c88)
- ブロック [`00af4c88`](#insn-00af4c88) 範囲 `[['00af4c88', '00af4c97']]`
  - `FALL_THROUGH` [`00af4c94`](#insn-00af4c94) → [`00af4c98`](#insn-00af4c98)
- ブロック [`00af4c98`](#insn-00af4c98) 範囲 `[['00af4c98', '00af4cab']]`

## 命令位置別の参照

- [`00af4aec`](#insn-00af4aec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4af0`](#insn-00af4af0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4af4`](#insn-00af4af4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4af8`](#insn-00af4af8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4b0c`](#insn-00af4b0c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4b34`](#insn-00af4b34) → [`00af4b70`](#insn-00af4b70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4b38`](#insn-00af4b38) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4b5c`](#insn-00af4b5c) → [`00af4b70`](#insn-00af4b70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4b6c`](#insn-00af4b6c) → [`00af4c24`](#insn-00af4c24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4b70`](#insn-00af4b70) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4b90`](#insn-00af4b90) → [`00af4c14`](#insn-00af4c14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4b94`](#insn-00af4b94) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4b98`](#insn-00af4b98) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4bac`](#insn-00af4bac) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00af4bb4`](#insn-00af4bb4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4bbc`](#insn-00af4bbc) → [`00af4c30`](#insn-00af4c30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4bc0`](#insn-00af4bc0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4bf0`](#insn-00af4bf0) → `002bfb38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4bf4`](#insn-00af4bf4) → [`00af4c88`](#insn-00af4c88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4bf8`](#insn-00af4bf8) → `002bfb40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4bf8`](#insn-00af4bf8) → `002bfb48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4bf8`](#insn-00af4bf8) → `002c46a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4bf8`](#insn-00af4bf8) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c00`](#insn-00af4c00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c04`](#insn-00af4c04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c08`](#insn-00af4c08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c0c`](#insn-00af4c0c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c10`](#insn-00af4c10) → [`0043be80`](../0043b/0043be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043be80` · 推定シンボル `None` · 推定型 `None`
- [`00af4c2c`](#insn-00af4c2c) → [`00af4c98`](#insn-00af4c98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c50`](#insn-00af4c50) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4c5c`](#insn-00af4c5c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4c80`](#insn-00af4c80) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c84`](#insn-00af4c84) → [`00af4bf8`](#insn-00af4bf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c88`](#insn-00af4c88) → `002bfb48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c88`](#insn-00af4c88) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c8c`](#insn-00af4c8c) → `002bfb38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c8c`](#insn-00af4c8c) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00af4c98`](#insn-00af4c98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4c9c`](#insn-00af4c9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4ca0`](#insn-00af4ca0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4ca4`](#insn-00af4ca4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af4aec`](#insn-00af4aec)

~~~json
{
  "source": "00af4aec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4af0`](#insn-00af4af0)

~~~json
{
  "source": "00af4af0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4af4`](#insn-00af4af4)

~~~json
{
  "source": "00af4af4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4af8`](#insn-00af4af8)

~~~json
{
  "source": "00af4af8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4b0c`](#insn-00af4b0c)

~~~json
{
  "source": "00af4b0c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4b34`](#insn-00af4b34)

~~~json
{
  "source": "00af4b34",
  "target": "00af4b70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4b38`](#insn-00af4b38)

~~~json
{
  "source": "00af4b38",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4b5c`](#insn-00af4b5c)

~~~json
{
  "source": "00af4b5c",
  "target": "00af4b70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4b6c`](#insn-00af4b6c)

~~~json
{
  "source": "00af4b6c",
  "target": "00af4c24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4b70`](#insn-00af4b70)

~~~json
{
  "source": "00af4b70",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4b90`](#insn-00af4b90)

~~~json
{
  "source": "00af4b90",
  "target": "00af4c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4b94`](#insn-00af4b94)

~~~json
{
  "source": "00af4b94",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4b98`](#insn-00af4b98)

~~~json
{
  "source": "00af4b98",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4bac`](#insn-00af4bac)

~~~json
{
  "source": "00af4bac",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4bb4`](#insn-00af4bb4)

~~~json
{
  "source": "00af4bb4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4bbc`](#insn-00af4bbc)

~~~json
{
  "source": "00af4bbc",
  "target": "00af4c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4bc0`](#insn-00af4bc0)

~~~json
{
  "source": "00af4bc0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4bf0`](#insn-00af4bf0)

~~~json
{
  "source": "00af4bf0",
  "target": "002bfb38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfb31",
  "offset": 7,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfb31",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4bf4`](#insn-00af4bf4)

~~~json
{
  "source": "00af4bf4",
  "target": "00af4c88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4bf8`](#insn-00af4bf8)

~~~json
{
  "source": "00af4bf8",
  "target": "002bfb40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfb31",
  "offset": 15,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfb31",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4bf8`](#insn-00af4bf8)

~~~json
{
  "source": "00af4bf8",
  "target": "002bfb48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfb31",
  "offset": 23,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfb31",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4bf8`](#insn-00af4bf8)

~~~json
{
  "source": "00af4bf8",
  "target": "002c46a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c45f6",
  "offset": 170,
  "size": 172,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c45f6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4bf8`](#insn-00af4bf8)

~~~json
{
  "source": "00af4bf8",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c46a2",
  "offset": 6,
  "size": 102,
  "datatype": "string",
  "bytes": "5a4e313161446f776e6c6f6164657238646f776e6c6f616445524b4e5374365f",
  "capture_start": "002c46a2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c00`](#insn-00af4c00)

~~~json
{
  "source": "00af4c00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c04`](#insn-00af4c04)

~~~json
{
  "source": "00af4c04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c08`](#insn-00af4c08)

~~~json
{
  "source": "00af4c08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c0c`](#insn-00af4c0c)

~~~json
{
  "source": "00af4c0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c10`](#insn-00af4c10)

~~~json
{
  "source": "00af4c10",
  "target": "0043be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4c2c`](#insn-00af4c2c)

~~~json
{
  "source": "00af4c2c",
  "target": "00af4c98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c50`](#insn-00af4c50)

~~~json
{
  "source": "00af4c50",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4c5c`](#insn-00af4c5c)

~~~json
{
  "source": "00af4c5c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4c80`](#insn-00af4c80)

~~~json
{
  "source": "00af4c80",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c45f6",
  "offset": 162,
  "size": 172,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c45f6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c84`](#insn-00af4c84)

~~~json
{
  "source": "00af4c84",
  "target": "00af4bf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c88`](#insn-00af4c88)

~~~json
{
  "source": "00af4c88",
  "target": "002bfb48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfb31",
  "offset": 23,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfb31",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c88`](#insn-00af4c88)

~~~json
{
  "source": "00af4c88",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c46a2",
  "offset": 6,
  "size": 102,
  "datatype": "string",
  "bytes": "5a4e313161446f776e6c6f6164657238646f776e6c6f616445524b4e5374365f",
  "capture_start": "002c46a2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c8c`](#insn-00af4c8c)

~~~json
{
  "source": "00af4c8c",
  "target": "002bfb38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfb31",
  "offset": 7,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfb31",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c8c`](#insn-00af4c8c)

~~~json
{
  "source": "00af4c8c",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c45f6",
  "offset": 162,
  "size": 172,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c45f6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00af4c98`](#insn-00af4c98)

~~~json
{
  "source": "00af4c98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4c9c`](#insn-00af4c9c)

~~~json
{
  "source": "00af4c9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4ca0`](#insn-00af4ca0)

~~~json
{
  "source": "00af4ca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4ca4`](#insn-00af4ca4)

~~~json
{
  "source": "00af4ca4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
