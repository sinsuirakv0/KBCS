# 00b5edac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5ddb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0032.md#compare-bf88db47a748492ae572ed00c0b18eba)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5edac",
  "name": "_ZNK8firebase4Path14FrontDirectoryEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f74ae868b1bd1b2025dafb333c9b7b08b35d28ce2b9e4dcadbd726a00dd08bb",
  "source_text_sha256": "9f74ae868b1bd1b2025dafb333c9b7b08b35d28ce2b9e4dcadbd726a00dd08bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5edac",
        "00b5ee83"
      ]
    ],
    "bytes_sha256": "5d3f7984718cc2149fb70b7bf1b1b188461961a0993d76ae0c798a3fea63845c",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5cc90](../00c5c/00c5cc90.md)
- [00c5cca0](../00c5c/00c5cca0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1331 bytes

~~~c

void _ZNK8firebase4Path14FrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_50;
  byte *local_48;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00b5ee3c:
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
      goto LAB_00b5ee5c;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00b5ee3c;
  _ZNK8firebase4Path14GetDirectoriesEv(&local_50);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  pbVar4 = local_50;
  if (local_50 != (byte *)0x0) {
    if (local_48 != local_50) {
      bVar1 = local_48[-0x18];
      pbVar5 = local_48 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_48 + -8));
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_48 = pbVar3;
      }
    }
    local_48 = pbVar4;
    _ZdlPv(local_50);
  }
LAB_00b5ee5c:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5edac"></a> `00b5edac` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5edb0"></a> `00b5edb0` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5edb4"></a> `00b5edb4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5edb8"></a> `00b5edb8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5edbc"></a> `00b5edbc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b5edc0"></a> `00b5edc0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5edc4"></a> `00b5edc4` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5edc8"></a> `00b5edc8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b5edcc"></a> `00b5edcc` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b5edd0"></a> `00b5edd0` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00b5edd4"></a> `00b5edd4` | `09 03 00 37` | tbnz w9,#0x0,0x00b5ee34 | `CONDITIONAL_JUMP`
<a id="insn-00b5edd8"></a> `00b5edd8` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5eddc"></a> `00b5eddc` | `08 03 00 b4` | cbz x8,0x00b5ee3c | `CONDITIONAL_JUMP`
<a id="insn-00b5ede0"></a> `00b5ede0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b5ede4"></a> `00b5ede4` | `af f7 03 94` | bl 0x00c5cca0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ede8"></a> `00b5ede8` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b5edec"></a> `00b5edec` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b5edf0"></a> `00b5edf0` | `a8 f7 03 94` | bl 0x00c5cc90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5edf4"></a> `00b5edf4` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-00b5edf8"></a> `00b5edf8` | `33 03 00 b4` | cbz x19,0x00b5ee5c | `CONDITIONAL_JUMP`
<a id="insn-00b5edfc"></a> `00b5edfc` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ee00"></a> `00b5ee00` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b5ee04"></a> `00b5ee04` | `60 02 00 54` | b.eq 0x00b5ee50 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee08"></a> `00b5ee08` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00b5ee0c"></a> `00b5ee0c` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b5ee10"></a> `00b5ee10` | `c9 00 00 37` | tbnz w9,#0x0,0x00b5ee28 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee14"></a> `00b5ee14` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00b5ee18"></a> `00b5ee18` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00b5ee1c"></a> `00b5ee1c` | `60 01 00 54` | b.eq 0x00b5ee48 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee20"></a> `00b5ee20` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b5ee24"></a> `00b5ee24` | `89 ff 07 36` | tbz w9,#0x0,0x00b5ee14 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee28"></a> `00b5ee28` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b5ee2c"></a> `00b5ee2c` | `49 e8 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ee30"></a> `00b5ee30` | `f9 ff ff 17` | b 0x00b5ee14 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ee34"></a> `00b5ee34` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ee38"></a> `00b5ee38` | `48 fd ff b5` | cbnz x8,0x00b5ede0 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee3c"></a> `00b5ee3c` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b5ee40"></a> `00b5ee40` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ee44"></a> `00b5ee44` | `06 00 00 14` | b 0x00b5ee5c | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ee48"></a> `00b5ee48` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b5ee4c"></a> `00b5ee4c` | `02 00 00 14` | b 0x00b5ee54 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ee50"></a> `00b5ee50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ee54"></a> `00b5ee54` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ee58"></a> `00b5ee58` | `3e e8 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ee5c"></a> `00b5ee5c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ee60"></a> `00b5ee60` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b5ee64"></a> `00b5ee64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5ee68"></a> `00b5ee68` | `c1 00 00 54` | b.ne 0x00b5ee80 | `CONDITIONAL_JUMP`
<a id="insn-00b5ee6c"></a> `00b5ee6c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5ee70"></a> `00b5ee70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5ee74"></a> `00b5ee74` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ee78"></a> `00b5ee78` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5ee7c"></a> `00b5ee7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5ee80"></a> `00b5ee80` | `40 e8 03 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5edac`](#insn-00b5edac) 範囲 `[['00b5edac', '00b5edd7']]`
  - `CONDITIONAL_JUMP` [`00b5edd4`](#insn-00b5edd4) → [`00b5ee34`](#insn-00b5ee34)
  - `FALL_THROUGH` [`00b5edd4`](#insn-00b5edd4) → [`00b5edd8`](#insn-00b5edd8)
- ブロック [`00b5edd8`](#insn-00b5edd8) 範囲 `[['00b5edd8', '00b5eddf']]`
  - `CONDITIONAL_JUMP` [`00b5eddc`](#insn-00b5eddc) → [`00b5ee3c`](#insn-00b5ee3c)
  - `FALL_THROUGH` [`00b5eddc`](#insn-00b5eddc) → [`00b5ede0`](#insn-00b5ede0)
- ブロック [`00b5ede0`](#insn-00b5ede0) 範囲 `[['00b5ede0', '00b5edfb']]`
  - `CONDITIONAL_JUMP` [`00b5edf8`](#insn-00b5edf8) → [`00b5ee5c`](#insn-00b5ee5c)
  - `FALL_THROUGH` [`00b5edf8`](#insn-00b5edf8) → [`00b5edfc`](#insn-00b5edfc)
- ブロック [`00b5edfc`](#insn-00b5edfc) 範囲 `[['00b5edfc', '00b5ee07']]`
  - `CONDITIONAL_JUMP` [`00b5ee04`](#insn-00b5ee04) → [`00b5ee50`](#insn-00b5ee50)
  - `FALL_THROUGH` [`00b5ee04`](#insn-00b5ee04) → [`00b5ee08`](#insn-00b5ee08)
- ブロック [`00b5ee08`](#insn-00b5ee08) 範囲 `[['00b5ee08', '00b5ee13']]`
  - `CONDITIONAL_JUMP` [`00b5ee10`](#insn-00b5ee10) → [`00b5ee28`](#insn-00b5ee28)
  - `FALL_THROUGH` [`00b5ee10`](#insn-00b5ee10) → [`00b5ee14`](#insn-00b5ee14)
- ブロック [`00b5ee14`](#insn-00b5ee14) 範囲 `[['00b5ee14', '00b5ee1f']]`
  - `CONDITIONAL_JUMP` [`00b5ee1c`](#insn-00b5ee1c) → [`00b5ee48`](#insn-00b5ee48)
  - `FALL_THROUGH` [`00b5ee1c`](#insn-00b5ee1c) → [`00b5ee20`](#insn-00b5ee20)
- ブロック [`00b5ee20`](#insn-00b5ee20) 範囲 `[['00b5ee20', '00b5ee27']]`
  - `CONDITIONAL_JUMP` [`00b5ee24`](#insn-00b5ee24) → [`00b5ee14`](#insn-00b5ee14)
  - `FALL_THROUGH` [`00b5ee24`](#insn-00b5ee24) → [`00b5ee28`](#insn-00b5ee28)
- ブロック [`00b5ee28`](#insn-00b5ee28) 範囲 `[['00b5ee28', '00b5ee33']]`
  - `UNCONDITIONAL_JUMP` [`00b5ee30`](#insn-00b5ee30) → [`00b5ee14`](#insn-00b5ee14)
- ブロック [`00b5ee34`](#insn-00b5ee34) 範囲 `[['00b5ee34', '00b5ee3b']]`
  - `CONDITIONAL_JUMP` [`00b5ee38`](#insn-00b5ee38) → [`00b5ede0`](#insn-00b5ede0)
  - `FALL_THROUGH` [`00b5ee38`](#insn-00b5ee38) → [`00b5ee3c`](#insn-00b5ee3c)
- ブロック [`00b5ee3c`](#insn-00b5ee3c) 範囲 `[['00b5ee3c', '00b5ee47']]`
  - `UNCONDITIONAL_JUMP` [`00b5ee44`](#insn-00b5ee44) → [`00b5ee5c`](#insn-00b5ee5c)
- ブロック [`00b5ee48`](#insn-00b5ee48) 範囲 `[['00b5ee48', '00b5ee4f']]`
  - `UNCONDITIONAL_JUMP` [`00b5ee4c`](#insn-00b5ee4c) → [`00b5ee54`](#insn-00b5ee54)
- ブロック [`00b5ee50`](#insn-00b5ee50) 範囲 `[['00b5ee50', '00b5ee53']]`
  - `FALL_THROUGH` [`00b5ee50`](#insn-00b5ee50) → [`00b5ee54`](#insn-00b5ee54)
- ブロック [`00b5ee54`](#insn-00b5ee54) 範囲 `[['00b5ee54', '00b5ee5b']]`
  - `FALL_THROUGH` [`00b5ee58`](#insn-00b5ee58) → [`00b5ee5c`](#insn-00b5ee5c)
- ブロック [`00b5ee5c`](#insn-00b5ee5c) 範囲 `[['00b5ee5c', '00b5ee6b']]`
  - `CONDITIONAL_JUMP` [`00b5ee68`](#insn-00b5ee68) → [`00b5ee80`](#insn-00b5ee80)
  - `FALL_THROUGH` [`00b5ee68`](#insn-00b5ee68) → [`00b5ee6c`](#insn-00b5ee6c)
- ブロック [`00b5ee6c`](#insn-00b5ee6c) 範囲 `[['00b5ee6c', '00b5ee7f']]`
- ブロック [`00b5ee80`](#insn-00b5ee80) 範囲 `[['00b5ee80', '00b5ee83']]`

## 命令位置別の参照

- [`00b5edb0`](#insn-00b5edb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edb4`](#insn-00b5edb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edb8`](#insn-00b5edb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edcc`](#insn-00b5edcc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edd4`](#insn-00b5edd4) → [`00b5ee34`](#insn-00b5ee34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5eddc`](#insn-00b5eddc) → [`00b5ee3c`](#insn-00b5ee3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ede4`](#insn-00b5ede4) → [`00c5cca0`](../00c5c/00c5cca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cca0` · 推定シンボル `None` · 推定型 `None`
- [`00b5ede8`](#insn-00b5ede8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edf0`](#insn-00b5edf0) → [`00c5cc90`](../00c5c/00c5cc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc90` · 推定シンボル `None` · 推定型 `None`
- [`00b5edf4`](#insn-00b5edf4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edf8`](#insn-00b5edf8) → [`00b5ee5c`](#insn-00b5ee5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5edfc`](#insn-00b5edfc) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee04`](#insn-00b5ee04) → [`00b5ee50`](#insn-00b5ee50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee10`](#insn-00b5ee10) → [`00b5ee28`](#insn-00b5ee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee1c`](#insn-00b5ee1c) → [`00b5ee48`](#insn-00b5ee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee24`](#insn-00b5ee24) → [`00b5ee14`](#insn-00b5ee14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee2c`](#insn-00b5ee2c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee30`](#insn-00b5ee30) → [`00b5ee14`](#insn-00b5ee14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee38`](#insn-00b5ee38) → [`00b5ede0`](#insn-00b5ede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee44`](#insn-00b5ee44) → [`00b5ee5c`](#insn-00b5ee5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee48`](#insn-00b5ee48) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee4c`](#insn-00b5ee4c) → [`00b5ee54`](#insn-00b5ee54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee54`](#insn-00b5ee54) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee58`](#insn-00b5ee58) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee60`](#insn-00b5ee60) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee68`](#insn-00b5ee68) → [`00b5ee80`](#insn-00b5ee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee6c`](#insn-00b5ee6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee70`](#insn-00b5ee70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee74`](#insn-00b5ee74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ee80`](#insn-00b5ee80) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5edb0`](#insn-00b5edb0)

~~~json
{
  "source": "00b5edb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edb4`](#insn-00b5edb4)

~~~json
{
  "source": "00b5edb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edb8`](#insn-00b5edb8)

~~~json
{
  "source": "00b5edb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edcc`](#insn-00b5edcc)

~~~json
{
  "source": "00b5edcc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edd4`](#insn-00b5edd4)

~~~json
{
  "source": "00b5edd4",
  "target": "00b5ee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5eddc`](#insn-00b5eddc)

~~~json
{
  "source": "00b5eddc",
  "target": "00b5ee3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ede4`](#insn-00b5ede4)

~~~json
{
  "source": "00b5ede4",
  "target": "00c5cca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ede8`](#insn-00b5ede8)

~~~json
{
  "source": "00b5ede8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edf0`](#insn-00b5edf0)

~~~json
{
  "source": "00b5edf0",
  "target": "00c5cc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5edf4`](#insn-00b5edf4)

~~~json
{
  "source": "00b5edf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edf8`](#insn-00b5edf8)

~~~json
{
  "source": "00b5edf8",
  "target": "00b5ee5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5edfc`](#insn-00b5edfc)

~~~json
{
  "source": "00b5edfc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee04`](#insn-00b5ee04)

~~~json
{
  "source": "00b5ee04",
  "target": "00b5ee50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee10`](#insn-00b5ee10)

~~~json
{
  "source": "00b5ee10",
  "target": "00b5ee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee1c`](#insn-00b5ee1c)

~~~json
{
  "source": "00b5ee1c",
  "target": "00b5ee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee24`](#insn-00b5ee24)

~~~json
{
  "source": "00b5ee24",
  "target": "00b5ee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee2c`](#insn-00b5ee2c)

~~~json
{
  "source": "00b5ee2c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ee30`](#insn-00b5ee30)

~~~json
{
  "source": "00b5ee30",
  "target": "00b5ee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee38`](#insn-00b5ee38)

~~~json
{
  "source": "00b5ee38",
  "target": "00b5ede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee44`](#insn-00b5ee44)

~~~json
{
  "source": "00b5ee44",
  "target": "00b5ee5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee48`](#insn-00b5ee48)

~~~json
{
  "source": "00b5ee48",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee4c`](#insn-00b5ee4c)

~~~json
{
  "source": "00b5ee4c",
  "target": "00b5ee54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee54`](#insn-00b5ee54)

~~~json
{
  "source": "00b5ee54",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee58`](#insn-00b5ee58)

~~~json
{
  "source": "00b5ee58",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ee60`](#insn-00b5ee60)

~~~json
{
  "source": "00b5ee60",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee68`](#insn-00b5ee68)

~~~json
{
  "source": "00b5ee68",
  "target": "00b5ee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee6c`](#insn-00b5ee6c)

~~~json
{
  "source": "00b5ee6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee70`](#insn-00b5ee70)

~~~json
{
  "source": "00b5ee70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee74`](#insn-00b5ee74)

~~~json
{
  "source": "00b5ee74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ee80`](#insn-00b5ee80)

~~~json
{
  "source": "00b5ee80",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
