# 00aa1cfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa1cb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1cb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-1147d4fc36cb8cfb6554a29f66a11fe7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0088.md#review-d04daec3a51c59885bbbddf6164aa660)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1cfc",
  "name": "FUN_00aa1cfc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "def3eb482c3ff3d8002b20609458522705263001015530462cf2f7e6fc34e9f9",
  "source_text_sha256": "def3eb482c3ff3d8002b20609458522705263001015530462cf2f7e6fc34e9f9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1cfc",
        "00aa1da3"
      ]
    ],
    "bytes_sha256": "01bcf68aad7d6c6fa93c37a9a4d98ffeaf4af14aa5d64300e86df1360c4d0da9",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00a9f124](../00a9f/00a9f124.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 557 bytes

~~~c

int FUN_00aa1cfc(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_0081f580();
  uVar4 = FUN_005c2710(lVar3 + (long)param_1 * 0x1f0 + 0x2678);
  lVar3 = FUN_0081f580();
  if ((uVar4 & 1) == 0) {
    iVar2 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0xa3c0);
  }
  else {
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9eee8);
    iVar2 = FUN_00a9f124(param_1,param_2,param_3,8,0);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa1cfc"></a> `00aa1cfc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa1d00"></a> `00aa1d00` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1d04"></a> `00aa1d04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1d08"></a> `00aa1d08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa1d0c"></a> `00aa1d0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa1d10"></a> `00aa1d10` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa1d14"></a> `00aa1d14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa1d18"></a> `00aa1d18` | `1a f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1d1c"></a> `00aa1d1c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa1d20"></a> `00aa1d20` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa1d24"></a> `00aa1d24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa1d28"></a> `00aa1d28` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1d2c"></a> `00aa1d2c` | `79 82 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1d30"></a> `00aa1d30` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa1d34"></a> `00aa1d34` | `13 f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1d38"></a> `00aa1d38` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa1d3c"></a> `00aa1d3c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa1d40"></a> `00aa1d40` | `f6 00 00 37` | tbnz w22,#0x0,0x00aa1d5c | `CONDITIONAL_JUMP`
<a id="insn-00aa1d44"></a> `00aa1d44` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa1d48"></a> `00aa1d48` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa1d4c"></a> `00aa1d4c` | `09 bf 93 52` | mov w9,#0x9df8 | `FALL_THROUGH`
<a id="insn-00aa1d50"></a> `00aa1d50` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa1d54"></a> `00aa1d54` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa1d58"></a> `00aa1d58` | `0f 00 00 14` | b 0x00aa1d94 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1d5c"></a> `00aa1d5c` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa1d60"></a> `00aa1d60` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa1d64"></a> `00aa1d64` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa1d68"></a> `00aa1d68` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa1d6c"></a> `00aa1d6c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa1d70"></a> `00aa1d70` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00aa1d74"></a> `00aa1d74` | `03 01 80 52` | mov w3,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1d78"></a> `00aa1d78` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aa1d7c"></a> `00aa1d7c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa1d80"></a> `00aa1d80` | `09 dd 9d 52` | mov w9,#0xeee8 | `FALL_THROUGH`
<a id="insn-00aa1d84"></a> `00aa1d84` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa1d88"></a> `00aa1d88` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa1d8c"></a> `00aa1d8c` | `e6 f4 ff 97` | bl 0x00a9f124 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1d90"></a> `00aa1d90` | `00 00 16 0b` | add w0,w0,w22 | `FALL_THROUGH`
<a id="insn-00aa1d94"></a> `00aa1d94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1d98"></a> `00aa1d98` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1d9c"></a> `00aa1d9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa1da0"></a> `00aa1da0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1cfc`](#insn-00aa1cfc) 範囲 `[['00aa1cfc', '00aa1d43']]`
  - `CONDITIONAL_JUMP` [`00aa1d40`](#insn-00aa1d40) → [`00aa1d5c`](#insn-00aa1d5c)
  - `FALL_THROUGH` [`00aa1d40`](#insn-00aa1d40) → [`00aa1d44`](#insn-00aa1d44)
- ブロック [`00aa1d44`](#insn-00aa1d44) 範囲 `[['00aa1d44', '00aa1d5b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1d58`](#insn-00aa1d58) → [`00aa1d94`](#insn-00aa1d94)
- ブロック [`00aa1d5c`](#insn-00aa1d5c) 範囲 `[['00aa1d5c', '00aa1d93']]`
  - `FALL_THROUGH` [`00aa1d90`](#insn-00aa1d90) → [`00aa1d94`](#insn-00aa1d94)
- ブロック [`00aa1d94`](#insn-00aa1d94) 範囲 `[['00aa1d94', '00aa1da3']]`

## 命令位置別の参照

- [`00aa1cfc`](#insn-00aa1cfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d00`](#insn-00aa1d00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d04`](#insn-00aa1d04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d18`](#insn-00aa1d18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d2c`](#insn-00aa1d2c) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d34`](#insn-00aa1d34) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d40`](#insn-00aa1d40) → [`00aa1d5c`](#insn-00aa1d5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d54`](#insn-00aa1d54) → `00239df8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa1d58`](#insn-00aa1d58) → [`00aa1d94`](#insn-00aa1d94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d8c`](#insn-00aa1d8c) → [`00a9f124`](../00a9f/00a9f124.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a9f124` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d94`](#insn-00aa1d94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d98`](#insn-00aa1d98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d9c`](#insn-00aa1d9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1cfc`](#insn-00aa1cfc)

~~~json
{
  "source": "00aa1cfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d00`](#insn-00aa1d00)

~~~json
{
  "source": "00aa1d00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d04`](#insn-00aa1d04)

~~~json
{
  "source": "00aa1d04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d18`](#insn-00aa1d18)

~~~json
{
  "source": "00aa1d18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1d2c`](#insn-00aa1d2c)

~~~json
{
  "source": "00aa1d2c",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1d34`](#insn-00aa1d34)

~~~json
{
  "source": "00aa1d34",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1d40`](#insn-00aa1d40)

~~~json
{
  "source": "00aa1d40",
  "target": "00aa1d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d54`](#insn-00aa1d54)

~~~json
{
  "source": "00aa1d54",
  "target": "00239df8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 41920,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa1d58`](#insn-00aa1d58)

~~~json
{
  "source": "00aa1d58",
  "target": "00aa1d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d8c`](#insn-00aa1d8c)

~~~json
{
  "source": "00aa1d8c",
  "target": "00a9f124",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1d94`](#insn-00aa1d94)

~~~json
{
  "source": "00aa1d94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d98`](#insn-00aa1d98)

~~~json
{
  "source": "00aa1d98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d9c`](#insn-00aa1d9c)

~~~json
{
  "source": "00aa1d9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
