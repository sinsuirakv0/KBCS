# 00aa3aec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa3aa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3aa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-9785c0743ec8fc79e544c05415b95739)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0089.md#review-6bc0e3f2437708e46c8f7ed200c7b54a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3aec",
  "name": "FUN_00aa3aec",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f6adfc34c6d3cb5e151327a4d0389f3adec4ce90739f31a21f983f0e5f6af67",
  "source_text_sha256": "7f6adfc34c6d3cb5e151327a4d0389f3adec4ce90739f31a21f983f0e5f6af67",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa3aec",
        "00aa3ba3"
      ]
    ],
    "bytes_sha256": "df61cc3d13165d869111f70efea35e1fdb74b5567703a6e5f12dbabbd1cfc57f",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c70](../00aa2/00aa2c70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 764 bytes

~~~c

ulong FUN_00aa3aec(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_0081f580();
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  lVar1 = FUN_0081f580();
  if ((uVar2 & 1) == 0) {
                    /* try { // try from 00aa3b4c to 00ba3b63 has its CatchHandler @ 00aa5a14 */
    uVar2 = (ulong)(*(int *)((long)__DT_JMPREL + lVar1 + ((long)param_2 + 2) * 0x1c4 + 0xa4c4) != 0)
    ;
  }
  else {
                    /* try { // try from 00aa3b64 to 00ba3b77 has its CatchHandler @ 00aa59fc */
    if (*(int *)(lVar1 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9eff4) == 0) {
      uVar2 = FUN_00aa2c70(lVar1,param_2,param_3,0x37);
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
<a id="insn-00aa3aec"></a> `00aa3aec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa3af0"></a> `00aa3af0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3af4"></a> `00aa3af4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3af8"></a> `00aa3af8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa3afc"></a> `00aa3afc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa3b00"></a> `00aa3b00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa3b04"></a> `00aa3b04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3b08"></a> `00aa3b08` | `9e ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b0c"></a> `00aa3b0c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa3b10"></a> `00aa3b10` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa3b14"></a> `00aa3b14` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3b18"></a> `00aa3b18` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa3b1c"></a> `00aa3b1c` | `fd 7a ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b20"></a> `00aa3b20` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa3b24"></a> `00aa3b24` | `97 ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b28"></a> `00aa3b28` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa3b2c"></a> `00aa3b2c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa3b30"></a> `00aa3b30` | `35 01 00 37` | tbnz w21,#0x0,0x00aa3b54 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b34"></a> `00aa3b34` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa3b38"></a> `00aa3b38` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3b3c"></a> `00aa3b3c` | `89 df 93 52` | mov w9,#0x9efc | `FALL_THROUGH`
<a id="insn-00aa3b40"></a> `00aa3b40` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3b44"></a> `00aa3b44` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3b48"></a> `00aa3b48` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa3b4c"></a> `00aa3b4c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa3b50"></a> `00aa3b50` | `0a 00 00 14` | b 0x00aa3b78 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa3b54"></a> `00aa3b54` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa3b58"></a> `00aa3b58` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3b5c"></a> `00aa3b5c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa3b60"></a> `00aa3b60` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa3b64"></a> `00aa3b64` | `89 fe 9d 52` | mov w9,#0xeff4 | `FALL_THROUGH`
<a id="insn-00aa3b68"></a> `00aa3b68` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3b6c"></a> `00aa3b6c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3b70"></a> `00aa3b70` | `c8 00 00 34` | cbz w8,0x00aa3b88 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b74"></a> `00aa3b74` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa3b78"></a> `00aa3b78` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3b7c"></a> `00aa3b7c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3b80"></a> `00aa3b80` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3b84"></a> `00aa3b84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa3b88"></a> `00aa3b88` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa3b8c"></a> `00aa3b8c` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa3b90"></a> `00aa3b90` | `e3 06 80 52` | mov w3,#0x37 | `FALL_THROUGH`
<a id="insn-00aa3b94"></a> `00aa3b94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3b98"></a> `00aa3b98` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3b9c"></a> `00aa3b9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3ba0"></a> `00aa3ba0` | `34 fc ff 17` | b 0x00aa2c70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa3aec`](#insn-00aa3aec) 範囲 `[['00aa3aec', '00aa3b33']]`
  - `CONDITIONAL_JUMP` [`00aa3b30`](#insn-00aa3b30) → [`00aa3b54`](#insn-00aa3b54)
  - `FALL_THROUGH` [`00aa3b30`](#insn-00aa3b30) → [`00aa3b34`](#insn-00aa3b34)
- ブロック [`00aa3b34`](#insn-00aa3b34) 範囲 `[['00aa3b34', '00aa3b4b']]`
  - `FALL_THROUGH` [`00aa3b48`](#insn-00aa3b48) → [`00aa3b4c`](#insn-00aa3b4c)
- ブロック [`00aa3b4c`](#insn-00aa3b4c) 範囲 `[['00aa3b4c', '00aa3b53']]`
  - `UNCONDITIONAL_JUMP` [`00aa3b50`](#insn-00aa3b50) → [`00aa3b78`](#insn-00aa3b78)
- ブロック [`00aa3b54`](#insn-00aa3b54) 範囲 `[['00aa3b54', '00aa3b63']]`
  - `FALL_THROUGH` [`00aa3b60`](#insn-00aa3b60) → [`00aa3b64`](#insn-00aa3b64)
- ブロック [`00aa3b64`](#insn-00aa3b64) 範囲 `[['00aa3b64', '00aa3b73']]`
  - `CONDITIONAL_JUMP` [`00aa3b70`](#insn-00aa3b70) → [`00aa3b88`](#insn-00aa3b88)
  - `FALL_THROUGH` [`00aa3b70`](#insn-00aa3b70) → [`00aa3b74`](#insn-00aa3b74)
- ブロック [`00aa3b74`](#insn-00aa3b74) 範囲 `[['00aa3b74', '00aa3b77']]`
  - `FALL_THROUGH` [`00aa3b74`](#insn-00aa3b74) → [`00aa3b78`](#insn-00aa3b78)
- ブロック [`00aa3b78`](#insn-00aa3b78) 範囲 `[['00aa3b78', '00aa3b87']]`
- ブロック [`00aa3b88`](#insn-00aa3b88) 範囲 `[['00aa3b88', '00aa3ba3']]`

## 命令位置別の参照

- [`00aa3aec`](#insn-00aa3aec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3af0`](#insn-00aa3af0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3af4`](#insn-00aa3af4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b08`](#insn-00aa3b08) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b1c`](#insn-00aa3b1c) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b24`](#insn-00aa3b24) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b30`](#insn-00aa3b30) → [`00aa3b54`](#insn-00aa3b54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b44`](#insn-00aa3b44) → `00239efc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa3b50`](#insn-00aa3b50) → [`00aa3b78`](#insn-00aa3b78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b70`](#insn-00aa3b70) → [`00aa3b88`](#insn-00aa3b88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b78`](#insn-00aa3b78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b7c`](#insn-00aa3b7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b80`](#insn-00aa3b80) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b94`](#insn-00aa3b94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b98`](#insn-00aa3b98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b9c`](#insn-00aa3b9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ba0`](#insn-00aa3ba0) → [`00aa2c70`](../00aa2/00aa2c70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa3aec`](#insn-00aa3aec)

~~~json
{
  "source": "00aa3aec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3af0`](#insn-00aa3af0)

~~~json
{
  "source": "00aa3af0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3af4`](#insn-00aa3af4)

~~~json
{
  "source": "00aa3af4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b08`](#insn-00aa3b08)

~~~json
{
  "source": "00aa3b08",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b1c`](#insn-00aa3b1c)

~~~json
{
  "source": "00aa3b1c",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b24`](#insn-00aa3b24)

~~~json
{
  "source": "00aa3b24",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b30`](#insn-00aa3b30)

~~~json
{
  "source": "00aa3b30",
  "target": "00aa3b54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b44`](#insn-00aa3b44)

~~~json
{
  "source": "00aa3b44",
  "target": "00239efc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42180,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa3b50`](#insn-00aa3b50)

~~~json
{
  "source": "00aa3b50",
  "target": "00aa3b78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b70`](#insn-00aa3b70)

~~~json
{
  "source": "00aa3b70",
  "target": "00aa3b88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b78`](#insn-00aa3b78)

~~~json
{
  "source": "00aa3b78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b7c`](#insn-00aa3b7c)

~~~json
{
  "source": "00aa3b7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b80`](#insn-00aa3b80)

~~~json
{
  "source": "00aa3b80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b94`](#insn-00aa3b94)

~~~json
{
  "source": "00aa3b94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b98`](#insn-00aa3b98)

~~~json
{
  "source": "00aa3b98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b9c`](#insn-00aa3b9c)

~~~json
{
  "source": "00aa3b9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ba0`](#insn-00aa3ba0)

~~~json
{
  "source": "00aa3ba0",
  "target": "00aa2c70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
