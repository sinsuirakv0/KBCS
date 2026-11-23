# 00aa2acc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aa2acc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa2/00aa2acc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0007.md#compare-50fdee201af41ff3068725608cc33463)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aa2b10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2b10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-8c8a10aefff8095fe9f04033729c3419)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2acc",
  "name": "FUN_00aa2acc",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b02557b9d97fcd023433b35a326e667cbdbe0c364ceab8eecb4f39e7d7a290b6",
  "source_text_sha256": "b02557b9d97fcd023433b35a326e667cbdbe0c364ceab8eecb4f39e7d7a290b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2acc",
        "00aa2b83"
      ]
    ],
    "bytes_sha256": "e73aadded87453f46d1f67a38e5e3937e02ee0ccb8801eda965157c8a81cc808",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 570 bytes

~~~c

ulong FUN_00aa2acc(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_0081f580();
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  lVar1 = FUN_0081f580();
  if ((uVar2 & 1) == 0) {
    uVar2 = (ulong)(*(int *)((long)__DT_JMPREL + lVar1 + ((long)param_2 + 2) * 0x1c4 + 0xa514) != 0)
    ;
  }
  else {
    if (*(int *)(lVar1 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9efc4) == 0) {
      uVar2 = FUN_00aa2c2c(lVar1,param_2,param_3,0x1d);
      return uVar2;
    }
    uVar2 = 1;
  }
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2acc"></a> `00aa2acc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa2ad0"></a> `00aa2ad0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2ad4"></a> `00aa2ad4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2ad8"></a> `00aa2ad8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa2adc"></a> `00aa2adc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa2ae0"></a> `00aa2ae0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa2ae4"></a> `00aa2ae4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa2ae8"></a> `00aa2ae8` | `a6 f2 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2aec"></a> `00aa2aec` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa2af0"></a> `00aa2af0` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa2af4"></a> `00aa2af4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa2af8"></a> `00aa2af8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa2afc"></a> `00aa2afc` | `05 7f ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b00"></a> `00aa2b00` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa2b04"></a> `00aa2b04` | `9f f2 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa2b08"></a> `00aa2b08` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa2b0c"></a> `00aa2b0c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa2b10"></a> `00aa2b10` | `35 01 00 37` | tbnz w21,#0x0,0x00aa2b34 | `CONDITIONAL_JUMP`
<a id="insn-00aa2b14"></a> `00aa2b14` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa2b18"></a> `00aa2b18` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa2b1c"></a> `00aa2b1c` | `89 e9 93 52` | mov w9,#0x9f4c | `FALL_THROUGH`
<a id="insn-00aa2b20"></a> `00aa2b20` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa2b24"></a> `00aa2b24` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa2b28"></a> `00aa2b28` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa2b2c"></a> `00aa2b2c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa2b30"></a> `00aa2b30` | `0a 00 00 14` | b 0x00aa2b58 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2b34"></a> `00aa2b34` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa2b38"></a> `00aa2b38` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa2b3c"></a> `00aa2b3c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa2b40"></a> `00aa2b40` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa2b44"></a> `00aa2b44` | `89 f8 9d 52` | mov w9,#0xefc4 | `FALL_THROUGH`
<a id="insn-00aa2b48"></a> `00aa2b48` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa2b4c"></a> `00aa2b4c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa2b50"></a> `00aa2b50` | `c8 00 00 34` | cbz w8,0x00aa2b68 | `CONDITIONAL_JUMP`
<a id="insn-00aa2b54"></a> `00aa2b54` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa2b58"></a> `00aa2b58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2b5c"></a> `00aa2b5c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2b60"></a> `00aa2b60` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa2b64"></a> `00aa2b64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa2b68"></a> `00aa2b68` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa2b6c"></a> `00aa2b6c` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa2b70"></a> `00aa2b70` | `a3 03 80 52` | mov w3,#0x1d | `FALL_THROUGH`
<a id="insn-00aa2b74"></a> `00aa2b74` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2b78"></a> `00aa2b78` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa2b7c"></a> `00aa2b7c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa2b80"></a> `00aa2b80` | `2b 00 00 14` | b 0x00aa2c2c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2acc`](#insn-00aa2acc) 範囲 `[['00aa2acc', '00aa2b13']]`
  - `CONDITIONAL_JUMP` [`00aa2b10`](#insn-00aa2b10) → [`00aa2b34`](#insn-00aa2b34)
  - `FALL_THROUGH` [`00aa2b10`](#insn-00aa2b10) → [`00aa2b14`](#insn-00aa2b14)
- ブロック [`00aa2b14`](#insn-00aa2b14) 範囲 `[['00aa2b14', '00aa2b33']]`
  - `UNCONDITIONAL_JUMP` [`00aa2b30`](#insn-00aa2b30) → [`00aa2b58`](#insn-00aa2b58)
- ブロック [`00aa2b34`](#insn-00aa2b34) 範囲 `[['00aa2b34', '00aa2b53']]`
  - `CONDITIONAL_JUMP` [`00aa2b50`](#insn-00aa2b50) → [`00aa2b68`](#insn-00aa2b68)
  - `FALL_THROUGH` [`00aa2b50`](#insn-00aa2b50) → [`00aa2b54`](#insn-00aa2b54)
- ブロック [`00aa2b54`](#insn-00aa2b54) 範囲 `[['00aa2b54', '00aa2b57']]`
  - `FALL_THROUGH` [`00aa2b54`](#insn-00aa2b54) → [`00aa2b58`](#insn-00aa2b58)
- ブロック [`00aa2b58`](#insn-00aa2b58) 範囲 `[['00aa2b58', '00aa2b67']]`
- ブロック [`00aa2b68`](#insn-00aa2b68) 範囲 `[['00aa2b68', '00aa2b83']]`

## 命令位置別の参照

- [`00aa2acc`](#insn-00aa2acc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ad0`](#insn-00aa2ad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ad4`](#insn-00aa2ad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2ae8`](#insn-00aa2ae8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa2afc`](#insn-00aa2afc) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b04`](#insn-00aa2b04) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b10`](#insn-00aa2b10) → [`00aa2b34`](#insn-00aa2b34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b24`](#insn-00aa2b24) → `00239f4c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa2b30`](#insn-00aa2b30) → [`00aa2b58`](#insn-00aa2b58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b50`](#insn-00aa2b50) → [`00aa2b68`](#insn-00aa2b68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b58`](#insn-00aa2b58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b5c`](#insn-00aa2b5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b60`](#insn-00aa2b60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b74`](#insn-00aa2b74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b78`](#insn-00aa2b78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b7c`](#insn-00aa2b7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2b80`](#insn-00aa2b80) → [`00aa2c2c`](00aa2c2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c2c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2acc`](#insn-00aa2acc)

~~~json
{
  "source": "00aa2acc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ad0`](#insn-00aa2ad0)

~~~json
{
  "source": "00aa2ad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ad4`](#insn-00aa2ad4)

~~~json
{
  "source": "00aa2ad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2ae8`](#insn-00aa2ae8)

~~~json
{
  "source": "00aa2ae8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2afc`](#insn-00aa2afc)

~~~json
{
  "source": "00aa2afc",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b04`](#insn-00aa2b04)

~~~json
{
  "source": "00aa2b04",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2b10`](#insn-00aa2b10)

~~~json
{
  "source": "00aa2b10",
  "target": "00aa2b34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b24`](#insn-00aa2b24)

~~~json
{
  "source": "00aa2b24",
  "target": "00239f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42260,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "50c0b100000000000204000001000000000000000000000058c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa2b30`](#insn-00aa2b30)

~~~json
{
  "source": "00aa2b30",
  "target": "00aa2b58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b50`](#insn-00aa2b50)

~~~json
{
  "source": "00aa2b50",
  "target": "00aa2b68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b58`](#insn-00aa2b58)

~~~json
{
  "source": "00aa2b58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b5c`](#insn-00aa2b5c)

~~~json
{
  "source": "00aa2b5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b60`](#insn-00aa2b60)

~~~json
{
  "source": "00aa2b60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b74`](#insn-00aa2b74)

~~~json
{
  "source": "00aa2b74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b78`](#insn-00aa2b78)

~~~json
{
  "source": "00aa2b78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b7c`](#insn-00aa2b7c)

~~~json
{
  "source": "00aa2b7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2b80`](#insn-00aa2b80)

~~~json
{
  "source": "00aa2b80",
  "target": "00aa2c2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
