# 00a4fdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a4fdbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4f/00a4fdbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0041.md#compare-52defc3387e3380db8156134086b82b3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a4fdbc",
  "name": "FUN_00a4fdbc",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28b563a30ccddac7ac82ec642e771b0a38a5e851b6c57f30ab7467f93bd983e3",
  "source_text_sha256": "28b563a30ccddac7ac82ec642e771b0a38a5e851b6c57f30ab7467f93bd983e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a4fdbc",
        "00a4fec7"
      ]
    ],
    "bytes_sha256": "4302dbe2f295a9825c2bf0c406b03fa32fdd166329af562167a4a45c4427c74f",
    "instruction_count": 67,
    "instruction_bytes": 268,
    "body_bytes": 268,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4b1c8](../00a4b/00a4b1c8.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1380 bytes

~~~c

void FUN_00a4fdbc(byte *param_1)

{
  byte bVar1;
  
  if ((param_1[0xd8] & 1) == 0) {
    bVar1 = param_1[0xc0];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xe8));
    bVar1 = param_1[0xc0];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0xa8];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xd0));
    bVar1 = param_1[0xa8];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x90];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xb8));
    bVar1 = param_1[0x90];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x78];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xa0));
    bVar1 = param_1[0x78];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x60];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x88));
    bVar1 = param_1[0x60];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x48];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x70));
    bVar1 = param_1[0x48];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x30];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x58));
    bVar1 = param_1[0x30];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x18];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x40));
    bVar1 = param_1[0x18];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *param_1;
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x28));
    bVar1 = *param_1;
  }
  if ((bVar1 & 1) != 0) {
    _ZdlPv(*(void **)(param_1 + 0x10));
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a4fdbc"></a> `00a4fdbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a4fdc0"></a> `00a4fdc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a4fdc4"></a> `00a4fdc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a4fdc8"></a> `00a4fdc8` | `08 60 43 39` | ldrb w8,[x0, #0xd8] | `FALL_THROUGH`
<a id="insn-00a4fdcc"></a> `00a4fdcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a4fdd0"></a> `00a4fdd0` | `c8 02 00 37` | tbnz w8,#0x0,0x00a4fe28 | `CONDITIONAL_JUMP`
<a id="insn-00a4fdd4"></a> `00a4fdd4` | `68 02 43 39` | ldrb w8,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00a4fdd8"></a> `00a4fdd8` | `08 03 00 37` | tbnz w8,#0x0,0x00a4fe38 | `CONDITIONAL_JUMP`
<a id="insn-00a4fddc"></a> `00a4fddc` | `68 a2 42 39` | ldrb w8,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-00a4fde0"></a> `00a4fde0` | `48 03 00 37` | tbnz w8,#0x0,0x00a4fe48 | `CONDITIONAL_JUMP`
<a id="insn-00a4fde4"></a> `00a4fde4` | `68 42 42 39` | ldrb w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00a4fde8"></a> `00a4fde8` | `88 03 00 37` | tbnz w8,#0x0,0x00a4fe58 | `CONDITIONAL_JUMP`
<a id="insn-00a4fdec"></a> `00a4fdec` | `68 e2 41 39` | ldrb w8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00a4fdf0"></a> `00a4fdf0` | `c8 03 00 37` | tbnz w8,#0x0,0x00a4fe68 | `CONDITIONAL_JUMP`
<a id="insn-00a4fdf4"></a> `00a4fdf4` | `68 82 41 39` | ldrb w8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00a4fdf8"></a> `00a4fdf8` | `08 04 00 37` | tbnz w8,#0x0,0x00a4fe78 | `CONDITIONAL_JUMP`
<a id="insn-00a4fdfc"></a> `00a4fdfc` | `68 22 41 39` | ldrb w8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00a4fe00"></a> `00a4fe00` | `48 04 00 37` | tbnz w8,#0x0,0x00a4fe88 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe04"></a> `00a4fe04` | `68 c2 40 39` | ldrb w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a4fe08"></a> `00a4fe08` | `88 04 00 37` | tbnz w8,#0x0,0x00a4fe98 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe0c"></a> `00a4fe0c` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a4fe10"></a> `00a4fe10` | `c8 04 00 37` | tbnz w8,#0x0,0x00a4fea8 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe14"></a> `00a4fe14` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00a4fe18"></a> `00a4fe18` | `08 05 00 37` | tbnz w8,#0x0,0x00a4feb8 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe1c"></a> `00a4fe1c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a4fe20"></a> `00a4fe20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a4fe24"></a> `00a4fe24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a4fe28"></a> `00a4fe28` | `60 76 40 f9` | ldr x0,[x19, #0xe8] | `FALL_THROUGH`
<a id="insn-00a4fe2c"></a> `00a4fe2c` | `4d 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe30"></a> `00a4fe30` | `68 02 43 39` | ldrb w8,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00a4fe34"></a> `00a4fe34` | `48 fd 07 36` | tbz w8,#0x0,0x00a4fddc | `CONDITIONAL_JUMP`
<a id="insn-00a4fe38"></a> `00a4fe38` | `60 6a 40 f9` | ldr x0,[x19, #0xd0] | `FALL_THROUGH`
<a id="insn-00a4fe3c"></a> `00a4fe3c` | `49 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe40"></a> `00a4fe40` | `68 a2 42 39` | ldrb w8,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-00a4fe44"></a> `00a4fe44` | `08 fd 07 36` | tbz w8,#0x0,0x00a4fde4 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe48"></a> `00a4fe48` | `60 5e 40 f9` | ldr x0,[x19, #0xb8] | `FALL_THROUGH`
<a id="insn-00a4fe4c"></a> `00a4fe4c` | `45 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe50"></a> `00a4fe50` | `68 42 42 39` | ldrb w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00a4fe54"></a> `00a4fe54` | `c8 fc 07 36` | tbz w8,#0x0,0x00a4fdec | `CONDITIONAL_JUMP`
<a id="insn-00a4fe58"></a> `00a4fe58` | `60 52 40 f9` | ldr x0,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00a4fe5c"></a> `00a4fe5c` | `41 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe60"></a> `00a4fe60` | `68 e2 41 39` | ldrb w8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00a4fe64"></a> `00a4fe64` | `88 fc 07 36` | tbz w8,#0x0,0x00a4fdf4 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe68"></a> `00a4fe68` | `60 46 40 f9` | ldr x0,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00a4fe6c"></a> `00a4fe6c` | `3d 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe70"></a> `00a4fe70` | `68 82 41 39` | ldrb w8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00a4fe74"></a> `00a4fe74` | `48 fc 07 36` | tbz w8,#0x0,0x00a4fdfc | `CONDITIONAL_JUMP`
<a id="insn-00a4fe78"></a> `00a4fe78` | `60 3a 40 f9` | ldr x0,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00a4fe7c"></a> `00a4fe7c` | `39 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe80"></a> `00a4fe80` | `68 22 41 39` | ldrb w8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00a4fe84"></a> `00a4fe84` | `08 fc 07 36` | tbz w8,#0x0,0x00a4fe04 | `CONDITIONAL_JUMP`
<a id="insn-00a4fe88"></a> `00a4fe88` | `60 2e 40 f9` | ldr x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00a4fe8c"></a> `00a4fe8c` | `35 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fe90"></a> `00a4fe90` | `68 c2 40 39` | ldrb w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a4fe94"></a> `00a4fe94` | `c8 fb 07 36` | tbz w8,#0x0,0x00a4fe0c | `CONDITIONAL_JUMP`
<a id="insn-00a4fe98"></a> `00a4fe98` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00a4fe9c"></a> `00a4fe9c` | `31 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4fea0"></a> `00a4fea0` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a4fea4"></a> `00a4fea4` | `88 fb 07 36` | tbz w8,#0x0,0x00a4fe14 | `CONDITIONAL_JUMP`
<a id="insn-00a4fea8"></a> `00a4fea8` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a4feac"></a> `00a4feac` | `2d 2c 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a4feb0"></a> `00a4feb0` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00a4feb4"></a> `00a4feb4` | `48 fb 07 36` | tbz w8,#0x0,0x00a4fe1c | `CONDITIONAL_JUMP`
<a id="insn-00a4feb8"></a> `00a4feb8` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a4febc"></a> `00a4febc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a4fec0"></a> `00a4fec0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a4fec4"></a> `00a4fec4` | `27 2c 06 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a4fdbc`](#insn-00a4fdbc) 範囲 `[['00a4fdbc', '00a4fdd3']]`
  - `CONDITIONAL_JUMP` [`00a4fdd0`](#insn-00a4fdd0) → [`00a4fe28`](#insn-00a4fe28)
  - `FALL_THROUGH` [`00a4fdd0`](#insn-00a4fdd0) → [`00a4fdd4`](#insn-00a4fdd4)
- ブロック [`00a4fdd4`](#insn-00a4fdd4) 範囲 `[['00a4fdd4', '00a4fddb']]`
  - `CONDITIONAL_JUMP` [`00a4fdd8`](#insn-00a4fdd8) → [`00a4fe38`](#insn-00a4fe38)
  - `FALL_THROUGH` [`00a4fdd8`](#insn-00a4fdd8) → [`00a4fddc`](#insn-00a4fddc)
- ブロック [`00a4fddc`](#insn-00a4fddc) 範囲 `[['00a4fddc', '00a4fde3']]`
  - `CONDITIONAL_JUMP` [`00a4fde0`](#insn-00a4fde0) → [`00a4fe48`](#insn-00a4fe48)
  - `FALL_THROUGH` [`00a4fde0`](#insn-00a4fde0) → [`00a4fde4`](#insn-00a4fde4)
- ブロック [`00a4fde4`](#insn-00a4fde4) 範囲 `[['00a4fde4', '00a4fdeb']]`
  - `CONDITIONAL_JUMP` [`00a4fde8`](#insn-00a4fde8) → [`00a4fe58`](#insn-00a4fe58)
  - `FALL_THROUGH` [`00a4fde8`](#insn-00a4fde8) → [`00a4fdec`](#insn-00a4fdec)
- ブロック [`00a4fdec`](#insn-00a4fdec) 範囲 `[['00a4fdec', '00a4fdf3']]`
  - `CONDITIONAL_JUMP` [`00a4fdf0`](#insn-00a4fdf0) → [`00a4fe68`](#insn-00a4fe68)
  - `FALL_THROUGH` [`00a4fdf0`](#insn-00a4fdf0) → [`00a4fdf4`](#insn-00a4fdf4)
- ブロック [`00a4fdf4`](#insn-00a4fdf4) 範囲 `[['00a4fdf4', '00a4fdfb']]`
  - `CONDITIONAL_JUMP` [`00a4fdf8`](#insn-00a4fdf8) → [`00a4fe78`](#insn-00a4fe78)
  - `FALL_THROUGH` [`00a4fdf8`](#insn-00a4fdf8) → [`00a4fdfc`](#insn-00a4fdfc)
- ブロック [`00a4fdfc`](#insn-00a4fdfc) 範囲 `[['00a4fdfc', '00a4fe03']]`
  - `CONDITIONAL_JUMP` [`00a4fe00`](#insn-00a4fe00) → [`00a4fe88`](#insn-00a4fe88)
  - `FALL_THROUGH` [`00a4fe00`](#insn-00a4fe00) → [`00a4fe04`](#insn-00a4fe04)
- ブロック [`00a4fe04`](#insn-00a4fe04) 範囲 `[['00a4fe04', '00a4fe0b']]`
  - `CONDITIONAL_JUMP` [`00a4fe08`](#insn-00a4fe08) → [`00a4fe98`](#insn-00a4fe98)
  - `FALL_THROUGH` [`00a4fe08`](#insn-00a4fe08) → [`00a4fe0c`](#insn-00a4fe0c)
- ブロック [`00a4fe0c`](#insn-00a4fe0c) 範囲 `[['00a4fe0c', '00a4fe13']]`
  - `CONDITIONAL_JUMP` [`00a4fe10`](#insn-00a4fe10) → [`00a4fea8`](#insn-00a4fea8)
  - `FALL_THROUGH` [`00a4fe10`](#insn-00a4fe10) → [`00a4fe14`](#insn-00a4fe14)
- ブロック [`00a4fe14`](#insn-00a4fe14) 範囲 `[['00a4fe14', '00a4fe1b']]`
  - `CONDITIONAL_JUMP` [`00a4fe18`](#insn-00a4fe18) → [`00a4feb8`](#insn-00a4feb8)
  - `FALL_THROUGH` [`00a4fe18`](#insn-00a4fe18) → [`00a4fe1c`](#insn-00a4fe1c)
- ブロック [`00a4fe1c`](#insn-00a4fe1c) 範囲 `[['00a4fe1c', '00a4fe27']]`
- ブロック [`00a4fe28`](#insn-00a4fe28) 範囲 `[['00a4fe28', '00a4fe37']]`
  - `CONDITIONAL_JUMP` [`00a4fe34`](#insn-00a4fe34) → [`00a4fddc`](#insn-00a4fddc)
  - `FALL_THROUGH` [`00a4fe34`](#insn-00a4fe34) → [`00a4fe38`](#insn-00a4fe38)
- ブロック [`00a4fe38`](#insn-00a4fe38) 範囲 `[['00a4fe38', '00a4fe47']]`
  - `CONDITIONAL_JUMP` [`00a4fe44`](#insn-00a4fe44) → [`00a4fde4`](#insn-00a4fde4)
  - `FALL_THROUGH` [`00a4fe44`](#insn-00a4fe44) → [`00a4fe48`](#insn-00a4fe48)
- ブロック [`00a4fe48`](#insn-00a4fe48) 範囲 `[['00a4fe48', '00a4fe57']]`
  - `CONDITIONAL_JUMP` [`00a4fe54`](#insn-00a4fe54) → [`00a4fdec`](#insn-00a4fdec)
  - `FALL_THROUGH` [`00a4fe54`](#insn-00a4fe54) → [`00a4fe58`](#insn-00a4fe58)
- ブロック [`00a4fe58`](#insn-00a4fe58) 範囲 `[['00a4fe58', '00a4fe67']]`
  - `CONDITIONAL_JUMP` [`00a4fe64`](#insn-00a4fe64) → [`00a4fdf4`](#insn-00a4fdf4)
  - `FALL_THROUGH` [`00a4fe64`](#insn-00a4fe64) → [`00a4fe68`](#insn-00a4fe68)
- ブロック [`00a4fe68`](#insn-00a4fe68) 範囲 `[['00a4fe68', '00a4fe77']]`
  - `CONDITIONAL_JUMP` [`00a4fe74`](#insn-00a4fe74) → [`00a4fdfc`](#insn-00a4fdfc)
  - `FALL_THROUGH` [`00a4fe74`](#insn-00a4fe74) → [`00a4fe78`](#insn-00a4fe78)
- ブロック [`00a4fe78`](#insn-00a4fe78) 範囲 `[['00a4fe78', '00a4fe87']]`
  - `CONDITIONAL_JUMP` [`00a4fe84`](#insn-00a4fe84) → [`00a4fe04`](#insn-00a4fe04)
  - `FALL_THROUGH` [`00a4fe84`](#insn-00a4fe84) → [`00a4fe88`](#insn-00a4fe88)
- ブロック [`00a4fe88`](#insn-00a4fe88) 範囲 `[['00a4fe88', '00a4fe97']]`
  - `CONDITIONAL_JUMP` [`00a4fe94`](#insn-00a4fe94) → [`00a4fe0c`](#insn-00a4fe0c)
  - `FALL_THROUGH` [`00a4fe94`](#insn-00a4fe94) → [`00a4fe98`](#insn-00a4fe98)
- ブロック [`00a4fe98`](#insn-00a4fe98) 範囲 `[['00a4fe98', '00a4fea7']]`
  - `CONDITIONAL_JUMP` [`00a4fea4`](#insn-00a4fea4) → [`00a4fe14`](#insn-00a4fe14)
  - `FALL_THROUGH` [`00a4fea4`](#insn-00a4fea4) → [`00a4fea8`](#insn-00a4fea8)
- ブロック [`00a4fea8`](#insn-00a4fea8) 範囲 `[['00a4fea8', '00a4feb7']]`
  - `CONDITIONAL_JUMP` [`00a4feb4`](#insn-00a4feb4) → [`00a4fe1c`](#insn-00a4fe1c)
  - `FALL_THROUGH` [`00a4feb4`](#insn-00a4feb4) → [`00a4feb8`](#insn-00a4feb8)
- ブロック [`00a4feb8`](#insn-00a4feb8) 範囲 `[['00a4feb8', '00a4fec7']]`

## 命令位置別の参照

- [`00a4fdbc`](#insn-00a4fdbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fdc0`](#insn-00a4fdc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fdd0`](#insn-00a4fdd0) → [`00a4fe28`](#insn-00a4fe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fdd8`](#insn-00a4fdd8) → [`00a4fe38`](#insn-00a4fe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fde0`](#insn-00a4fde0) → [`00a4fe48`](#insn-00a4fe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fde8`](#insn-00a4fde8) → [`00a4fe58`](#insn-00a4fe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fdf0`](#insn-00a4fdf0) → [`00a4fe68`](#insn-00a4fe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fdf8`](#insn-00a4fdf8) → [`00a4fe78`](#insn-00a4fe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe00`](#insn-00a4fe00) → [`00a4fe88`](#insn-00a4fe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe08`](#insn-00a4fe08) → [`00a4fe98`](#insn-00a4fe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe10`](#insn-00a4fe10) → [`00a4fea8`](#insn-00a4fea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe18`](#insn-00a4fe18) → [`00a4feb8`](#insn-00a4feb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe1c`](#insn-00a4fe1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe20`](#insn-00a4fe20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe2c`](#insn-00a4fe2c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe34`](#insn-00a4fe34) → [`00a4fddc`](#insn-00a4fddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe3c`](#insn-00a4fe3c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe44`](#insn-00a4fe44) → [`00a4fde4`](#insn-00a4fde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe4c`](#insn-00a4fe4c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe54`](#insn-00a4fe54) → [`00a4fdec`](#insn-00a4fdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe5c`](#insn-00a4fe5c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe64`](#insn-00a4fe64) → [`00a4fdf4`](#insn-00a4fdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe6c`](#insn-00a4fe6c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe74`](#insn-00a4fe74) → [`00a4fdfc`](#insn-00a4fdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe7c`](#insn-00a4fe7c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe84`](#insn-00a4fe84) → [`00a4fe04`](#insn-00a4fe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe8c`](#insn-00a4fe8c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe94`](#insn-00a4fe94) → [`00a4fe0c`](#insn-00a4fe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fe9c`](#insn-00a4fe9c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4fea4`](#insn-00a4fea4) → [`00a4fe14`](#insn-00a4fe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4feac`](#insn-00a4feac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a4feb4`](#insn-00a4feb4) → [`00a4fe1c`](#insn-00a4fe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4febc`](#insn-00a4febc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fec0`](#insn-00a4fec0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a4fec4`](#insn-00a4fec4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a4fdbc`](#insn-00a4fdbc)

~~~json
{
  "source": "00a4fdbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fdc0`](#insn-00a4fdc0)

~~~json
{
  "source": "00a4fdc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fdd0`](#insn-00a4fdd0)

~~~json
{
  "source": "00a4fdd0",
  "target": "00a4fe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fdd8`](#insn-00a4fdd8)

~~~json
{
  "source": "00a4fdd8",
  "target": "00a4fe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fde0`](#insn-00a4fde0)

~~~json
{
  "source": "00a4fde0",
  "target": "00a4fe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fde8`](#insn-00a4fde8)

~~~json
{
  "source": "00a4fde8",
  "target": "00a4fe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fdf0`](#insn-00a4fdf0)

~~~json
{
  "source": "00a4fdf0",
  "target": "00a4fe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fdf8`](#insn-00a4fdf8)

~~~json
{
  "source": "00a4fdf8",
  "target": "00a4fe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe00`](#insn-00a4fe00)

~~~json
{
  "source": "00a4fe00",
  "target": "00a4fe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe08`](#insn-00a4fe08)

~~~json
{
  "source": "00a4fe08",
  "target": "00a4fe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe10`](#insn-00a4fe10)

~~~json
{
  "source": "00a4fe10",
  "target": "00a4fea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe18`](#insn-00a4fe18)

~~~json
{
  "source": "00a4fe18",
  "target": "00a4feb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe1c`](#insn-00a4fe1c)

~~~json
{
  "source": "00a4fe1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe20`](#insn-00a4fe20)

~~~json
{
  "source": "00a4fe20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe2c`](#insn-00a4fe2c)

~~~json
{
  "source": "00a4fe2c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe34`](#insn-00a4fe34)

~~~json
{
  "source": "00a4fe34",
  "target": "00a4fddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe3c`](#insn-00a4fe3c)

~~~json
{
  "source": "00a4fe3c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe44`](#insn-00a4fe44)

~~~json
{
  "source": "00a4fe44",
  "target": "00a4fde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe4c`](#insn-00a4fe4c)

~~~json
{
  "source": "00a4fe4c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe54`](#insn-00a4fe54)

~~~json
{
  "source": "00a4fe54",
  "target": "00a4fdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe5c`](#insn-00a4fe5c)

~~~json
{
  "source": "00a4fe5c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe64`](#insn-00a4fe64)

~~~json
{
  "source": "00a4fe64",
  "target": "00a4fdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe6c`](#insn-00a4fe6c)

~~~json
{
  "source": "00a4fe6c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe74`](#insn-00a4fe74)

~~~json
{
  "source": "00a4fe74",
  "target": "00a4fdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe7c`](#insn-00a4fe7c)

~~~json
{
  "source": "00a4fe7c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe84`](#insn-00a4fe84)

~~~json
{
  "source": "00a4fe84",
  "target": "00a4fe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe8c`](#insn-00a4fe8c)

~~~json
{
  "source": "00a4fe8c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fe94`](#insn-00a4fe94)

~~~json
{
  "source": "00a4fe94",
  "target": "00a4fe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fe9c`](#insn-00a4fe9c)

~~~json
{
  "source": "00a4fe9c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4fea4`](#insn-00a4fea4)

~~~json
{
  "source": "00a4fea4",
  "target": "00a4fe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4feac`](#insn-00a4feac)

~~~json
{
  "source": "00a4feac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a4feb4`](#insn-00a4feb4)

~~~json
{
  "source": "00a4feb4",
  "target": "00a4fe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4febc`](#insn-00a4febc)

~~~json
{
  "source": "00a4febc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fec0`](#insn-00a4fec0)

~~~json
{
  "source": "00a4fec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a4fec4`](#insn-00a4fec4)

~~~json
{
  "source": "00a4fec4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
