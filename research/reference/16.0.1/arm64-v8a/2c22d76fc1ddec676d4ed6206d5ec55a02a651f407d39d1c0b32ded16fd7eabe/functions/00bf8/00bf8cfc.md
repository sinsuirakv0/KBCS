# 00bf8cfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf88d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-58973895092ede80ee34c7bd1ee8bc78)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf8d98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8d98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-0d1b9e660ab7e98189673daee995927e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf8cfc",
  "name": "_ZNSt6__ndk112system_errorC2EiRKNS_14error_categoryERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a16dcb903fd0fdf89f08b2e9376d1b64bc006e58117febc1e3ad56aa39cf662",
  "source_text_sha256": "1a16dcb903fd0fdf89f08b2e9376d1b64bc006e58117febc1e3ad56aa39cf662",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf8cfc",
        "00bf8dbb"
      ]
    ],
    "bytes_sha256": "92ed6ecb6fb1051dfb2b5965aadf4873b926cfeb5da66d6916beaaad46022236",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [00bf8a14](../00bf8/00bf8a14.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5dfa0](../00c5d/00c5dfa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1050 bytes

~~~c

void _ZNSt6__ndk112system_errorC2EiRKNS_14error_categoryERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (long *param_1,undefined4 param_2,long param_3,ulong *param_4)

{
  undefined *puVar1;
  ulong local_70;
  ulong uStack_68;
  void *local_60;
  undefined4 local_58 [2];
  long local_50;
  byte local_48 [16];
  void *local_38;
  
  local_58[0] = param_2;
  local_50 = param_3;
  if ((*param_4 & 1) == 0) {
    uStack_68 = param_4[1];
    local_70 = *param_4;
    local_60 = (void *)param_4[2];
  }
  else {
    FUN_0043bb20(&local_70,param_4[2],param_4[1]);
  }
  FUN_00bf8a14(local_48,local_58,&local_70);
  _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  puVar1 = PTR__ZTVNSt6__ndk112system_errorE_00c9bad0;
  *(undefined4 *)(param_1 + 2) = param_2;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[3] = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf8cfc"></a> `00bf8cfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf8d00"></a> `00bf8d00` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf8d04"></a> `00bf8d04` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf8d08"></a> `00bf8d08` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf8d0c"></a> `00bf8d0c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf8d10"></a> `00bf8d10` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bf8d14"></a> `00bf8d14` | `68 00 40 39` | ldrb w8,[x3] | `FALL_THROUGH`
<a id="insn-00bf8d18"></a> `00bf8d18` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bf8d1c"></a> `00bf8d1c` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00bf8d20"></a> `00bf8d20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bf8d24"></a> `00bf8d24` | `e1 1b 00 b9` | str w1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf8d28"></a> `00bf8d28` | `e2 13 00 f9` | str x2,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf8d2c"></a> `00bf8d2c` | `c8 00 00 37` | tbnz w8,#0x0,0x00bf8d44 | `CONDITIONAL_JUMP`
<a id="insn-00bf8d30"></a> `00bf8d30` | `60 00 c0 3d` | ldr q0,[x3] | `FALL_THROUGH`
<a id="insn-00bf8d34"></a> `00bf8d34` | `68 08 40 f9` | ldr x8,[x3, #0x10] | `FALL_THROUGH`
<a id="insn-00bf8d38"></a> `00bf8d38` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf8d3c"></a> `00bf8d3c` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf8d40"></a> `00bf8d40` | `04 00 00 14` | b 0x00bf8d50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf8d44"></a> `00bf8d44` | `62 84 40 a9` | ldp x2,x1,[x3, #0x8] | `FALL_THROUGH`
<a id="insn-00bf8d48"></a> `00bf8d48` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf8d4c"></a> `00bf8d4c` | `75 0b e1 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8d50"></a> `00bf8d50` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf8d54"></a> `00bf8d54` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf8d58"></a> `00bf8d58` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bf8d5c"></a> `00bf8d5c` | `2e ff ff 97` | bl 0x00bf8a14 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8d60"></a> `00bf8d60` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf8d64"></a> `00bf8d64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf8d68"></a> `00bf8d68` | `8e 94 01 94` | bl 0x00c5dfa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8d6c"></a> `00bf8d6c` | `a8 83 5e 38` | ldurb w8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bf8d70"></a> `00bf8d70` | `68 00 00 36` | tbz w8,#0x0,0x00bf8d7c | `CONDITIONAL_JUMP`
<a id="insn-00bf8d74"></a> `00bf8d74` | `a0 83 5f f8` | ldur x0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bf8d78"></a> `00bf8d78` | `4e 7c 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8d7c"></a> `00bf8d7c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf8d80"></a> `00bf8d80` | `68 00 00 36` | tbz w8,#0x0,0x00bf8d8c | `CONDITIONAL_JUMP`
<a id="insn-00bf8d84"></a> `00bf8d84` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf8d88"></a> `00bf8d88` | `4a 7c 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8d8c"></a> `00bf8d8c` | `08 05 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bf8d90"></a> `00bf8d90` | `08 69 45 f9` | ldr x8,[x8, #0xad0] | `FALL_THROUGH`
<a id="insn-00bf8d94"></a> `00bf8d94` | `95 12 00 b9` | str w21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bf8d98"></a> `00bf8d98` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bf8d9c"></a> `00bf8d9c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bf8da0"></a> `00bf8da0` | `93 0e 00 f9` | str x19,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bf8da4"></a> `00bf8da4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf8da8"></a> `00bf8da8` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf8dac"></a> `00bf8dac` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf8db0"></a> `00bf8db0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf8db4"></a> `00bf8db4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf8db8"></a> `00bf8db8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf8cfc`](#insn-00bf8cfc) 範囲 `[['00bf8cfc', '00bf8d2f']]`
  - `CONDITIONAL_JUMP` [`00bf8d2c`](#insn-00bf8d2c) → [`00bf8d44`](#insn-00bf8d44)
  - `FALL_THROUGH` [`00bf8d2c`](#insn-00bf8d2c) → [`00bf8d30`](#insn-00bf8d30)
- ブロック [`00bf8d30`](#insn-00bf8d30) 範囲 `[['00bf8d30', '00bf8d43']]`
  - `UNCONDITIONAL_JUMP` [`00bf8d40`](#insn-00bf8d40) → [`00bf8d50`](#insn-00bf8d50)
- ブロック [`00bf8d44`](#insn-00bf8d44) 範囲 `[['00bf8d44', '00bf8d4f']]`
  - `FALL_THROUGH` [`00bf8d4c`](#insn-00bf8d4c) → [`00bf8d50`](#insn-00bf8d50)
- ブロック [`00bf8d50`](#insn-00bf8d50) 範囲 `[['00bf8d50', '00bf8d73']]`
  - `CONDITIONAL_JUMP` [`00bf8d70`](#insn-00bf8d70) → [`00bf8d7c`](#insn-00bf8d7c)
  - `FALL_THROUGH` [`00bf8d70`](#insn-00bf8d70) → [`00bf8d74`](#insn-00bf8d74)
- ブロック [`00bf8d74`](#insn-00bf8d74) 範囲 `[['00bf8d74', '00bf8d7b']]`
  - `FALL_THROUGH` [`00bf8d78`](#insn-00bf8d78) → [`00bf8d7c`](#insn-00bf8d7c)
- ブロック [`00bf8d7c`](#insn-00bf8d7c) 範囲 `[['00bf8d7c', '00bf8d83']]`
  - `CONDITIONAL_JUMP` [`00bf8d80`](#insn-00bf8d80) → [`00bf8d8c`](#insn-00bf8d8c)
  - `FALL_THROUGH` [`00bf8d80`](#insn-00bf8d80) → [`00bf8d84`](#insn-00bf8d84)
- ブロック [`00bf8d84`](#insn-00bf8d84) 範囲 `[['00bf8d84', '00bf8d8b']]`
  - `FALL_THROUGH` [`00bf8d88`](#insn-00bf8d88) → [`00bf8d8c`](#insn-00bf8d8c)
- ブロック [`00bf8d8c`](#insn-00bf8d8c) 範囲 `[['00bf8d8c', '00bf8dbb']]`

## 命令位置別の参照

- [`00bf8d04`](#insn-00bf8d04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d08`](#insn-00bf8d08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d0c`](#insn-00bf8d0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d24`](#insn-00bf8d24) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d28`](#insn-00bf8d28) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d2c`](#insn-00bf8d2c) → [`00bf8d44`](#insn-00bf8d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d38`](#insn-00bf8d38) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d3c`](#insn-00bf8d3c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d40`](#insn-00bf8d40) → [`00bf8d50`](#insn-00bf8d50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d4c`](#insn-00bf8d4c) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d5c`](#insn-00bf8d5c) → [`00bf8a14`](00bf8a14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf8a14` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d68`](#insn-00bf8d68) → [`00c5dfa0`](../00c5d/00c5dfa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dfa0` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d6c`](#insn-00bf8d6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d70`](#insn-00bf8d70) → [`00bf8d7c`](#insn-00bf8d7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d74`](#insn-00bf8d74) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d78`](#insn-00bf8d78) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d7c`](#insn-00bf8d7c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d80`](#insn-00bf8d80) → [`00bf8d8c`](#insn-00bf8d8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d84`](#insn-00bf8d84) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d88`](#insn-00bf8d88) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bf8d90`](#insn-00bf8d90) → `00c9bad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bf8d9c`](#insn-00bf8d9c) → `00c92b70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bf8da4`](#insn-00bf8da4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8da8`](#insn-00bf8da8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8dac`](#insn-00bf8dac) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf8d04`](#insn-00bf8d04)

~~~json
{
  "source": "00bf8d04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d08`](#insn-00bf8d08)

~~~json
{
  "source": "00bf8d08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d0c`](#insn-00bf8d0c)

~~~json
{
  "source": "00bf8d0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d24`](#insn-00bf8d24)

~~~json
{
  "source": "00bf8d24",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d28`](#insn-00bf8d28)

~~~json
{
  "source": "00bf8d28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d2c`](#insn-00bf8d2c)

~~~json
{
  "source": "00bf8d2c",
  "target": "00bf8d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d38`](#insn-00bf8d38)

~~~json
{
  "source": "00bf8d38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d3c`](#insn-00bf8d3c)

~~~json
{
  "source": "00bf8d3c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d40`](#insn-00bf8d40)

~~~json
{
  "source": "00bf8d40",
  "target": "00bf8d50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d4c`](#insn-00bf8d4c)

~~~json
{
  "source": "00bf8d4c",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8d5c`](#insn-00bf8d5c)

~~~json
{
  "source": "00bf8d5c",
  "target": "00bf8a14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8d68`](#insn-00bf8d68)

~~~json
{
  "source": "00bf8d68",
  "target": "00c5dfa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8d6c`](#insn-00bf8d6c)

~~~json
{
  "source": "00bf8d6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d70`](#insn-00bf8d70)

~~~json
{
  "source": "00bf8d70",
  "target": "00bf8d7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d74`](#insn-00bf8d74)

~~~json
{
  "source": "00bf8d74",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d78`](#insn-00bf8d78)

~~~json
{
  "source": "00bf8d78",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8d7c`](#insn-00bf8d7c)

~~~json
{
  "source": "00bf8d7c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d80`](#insn-00bf8d80)

~~~json
{
  "source": "00bf8d80",
  "target": "00bf8d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d84`](#insn-00bf8d84)

~~~json
{
  "source": "00bf8d84",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8d88`](#insn-00bf8d88)

~~~json
{
  "source": "00bf8d88",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8d90`](#insn-00bf8d90)

~~~json
{
  "source": "00bf8d90",
  "target": "00c9bad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bad0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bf8d9c`](#insn-00bf8d9c)

~~~json
{
  "source": "00bf8d9c",
  "target": "00c92b70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92b60",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bf8da4`](#insn-00bf8da4)

~~~json
{
  "source": "00bf8da4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8da8`](#insn-00bf8da8)

~~~json
{
  "source": "00bf8da8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8dac`](#insn-00bf8dac)

~~~json
{
  "source": "00bf8dac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
