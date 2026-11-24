# 007bbbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0128.md#review-a283c03ddc627cfb02cfeaf2d1081776)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0024.md#review-a283c03ddc627cfb02cfeaf2d1081776)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007bbbec",
  "name": "FUN_007bbbec",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "589f7514852d7414548427c155f2f7446517e1d2d39839419cdd2341af6ba70a",
  "source_text_sha256": "589f7514852d7414548427c155f2f7446517e1d2d39839419cdd2341af6ba70a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007bbbec",
        "007bbc6f"
      ]
    ],
    "bytes_sha256": "41dc798d32bba8929f4caa1597ea91920e507d6977591f29f606630ce1fc7506",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [006bed1c](../006be/006bed1c.md)
- [007bda04](../007bd/007bda04.md)
- [007df0a8](../007df/007df0a8.md)
- [00802678](../00802/00802678.md)
- [00933edc](../00933/00933edc.md)
- [009d9790](../009d9/009d9790.md)
- [00a47d08](../00a47/00a47d08.md)
- [00afdfe4](../00afd/00afdfe4.md)
- [00aff204](../00aff/00aff204.md)

## 呼び出し先

- [0080018c](../00800/0080018c.md)
- [00802ea0](../00802/00802ea0.md)
- [008077b8](../00807/008077b8.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1035 bytes

~~~c

undefined8 FUN_007bbbec(long param_1)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  undefined8 uVar4;
  
  lVar2 = FUN_008514b8();
  iVar1 = FUN_0080018c(*(undefined4 *)(BYTE_ARRAY_0038f27d + lVar2 + 7));
  if ((((iVar1 == 0) && (*(int *)((long)&QWORD_00344440 + param_1) == 0x30)) &&
      (iVar1 = FUN_00802ea0(), iVar1 == 3)) &&
     ((uVar3 = FUN_008077b8(0,0x30,3,0), (uVar3 & 1) != 0 && (*(char *)(param_1 + 0x15a0) == '\0')))
     ) {
    uVar4 = 1;
  }
  else {
                    /* try { // try from 007bbc58 to 008bbe6b has its CatchHandler @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bbc58 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bbeb4 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bcdd0 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007be150 with catch @ 007bbc58
                        */
    uVar4 = 0;
  }
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007bbbec"></a> `007bbbec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007bbbf0"></a> `007bbbf0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007bbbf4"></a> `007bbbf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007bbbf8"></a> `007bbbf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007bbbfc"></a> `007bbbfc` | `2f 56 02 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-007bbc00"></a> `007bbc00` | `88 50 9e 52` | mov w8,#0xf284 | `FALL_THROUGH`
<a id="insn-007bbc04"></a> `007bbc04` | `08 07 a0 72` | movk w8,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-007bbc08"></a> `007bbc08` | `00 68 68 b8` | ldr w0,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bbc0c"></a> `007bbc0c` | `60 11 01 94` | bl 0x0080018c | `UNCONDITIONAL_CALL`
<a id="insn-007bbc10"></a> `007bbc10` | `40 02 00 35` | cbnz w0,0x007bbc58 | `CONDITIONAL_JUMP`
<a id="insn-007bbc14"></a> `007bbc14` | `08 88 88 52` | mov w8,#0x4440 | `FALL_THROUGH`
<a id="insn-007bbc18"></a> `007bbc18` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-007bbc1c"></a> `007bbc1c` | `68 6a 68 b8` | ldr w8,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007bbc20"></a> `007bbc20` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-007bbc24"></a> `007bbc24` | `a1 01 00 54` | b.ne 0x007bbc58 | `CONDITIONAL_JUMP`
<a id="insn-007bbc28"></a> `007bbc28` | `9e 1c 01 94` | bl 0x00802ea0 | `UNCONDITIONAL_CALL`
<a id="insn-007bbc2c"></a> `007bbc2c` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-007bbc30"></a> `007bbc30` | `41 01 00 54` | b.ne 0x007bbc58 | `CONDITIONAL_JUMP`
<a id="insn-007bbc34"></a> `007bbc34` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bbc38"></a> `007bbc38` | `01 06 80 52` | mov w1,#0x30 | `FALL_THROUGH`
<a id="insn-007bbc3c"></a> `007bbc3c` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-007bbc40"></a> `007bbc40` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-007bbc44"></a> `007bbc44` | `dd 2e 01 94` | bl 0x008077b8 | `UNCONDITIONAL_CALL`
<a id="insn-007bbc48"></a> `007bbc48` | `80 00 00 36` | tbz w0,#0x0,0x007bbc58 | `CONDITIONAL_JUMP`
<a id="insn-007bbc4c"></a> `007bbc4c` | `08 b4 82 52` | mov w8,#0x15a0 | `FALL_THROUGH`
<a id="insn-007bbc50"></a> `007bbc50` | `68 6a 68 38` | ldrb w8,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-007bbc54"></a> `007bbc54` | `a8 00 00 34` | cbz w8,0x007bbc68 | `CONDITIONAL_JUMP`
<a id="insn-007bbc58"></a> `007bbc58` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-007bbc5c"></a> `007bbc5c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007bbc60"></a> `007bbc60` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007bbc64"></a> `007bbc64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007bbc68"></a> `007bbc68` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007bbc6c"></a> `007bbc6c` | `fc ff ff 17` | b 0x007bbc5c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`007bbbec`](#insn-007bbbec) 範囲 `[['007bbbec', '007bbc13']]`
  - `CONDITIONAL_JUMP` [`007bbc10`](#insn-007bbc10) → [`007bbc58`](#insn-007bbc58)
  - `FALL_THROUGH` [`007bbc10`](#insn-007bbc10) → [`007bbc14`](#insn-007bbc14)
- ブロック [`007bbc14`](#insn-007bbc14) 範囲 `[['007bbc14', '007bbc27']]`
  - `CONDITIONAL_JUMP` [`007bbc24`](#insn-007bbc24) → [`007bbc58`](#insn-007bbc58)
  - `FALL_THROUGH` [`007bbc24`](#insn-007bbc24) → [`007bbc28`](#insn-007bbc28)
- ブロック [`007bbc28`](#insn-007bbc28) 範囲 `[['007bbc28', '007bbc33']]`
  - `CONDITIONAL_JUMP` [`007bbc30`](#insn-007bbc30) → [`007bbc58`](#insn-007bbc58)
  - `FALL_THROUGH` [`007bbc30`](#insn-007bbc30) → [`007bbc34`](#insn-007bbc34)
- ブロック [`007bbc34`](#insn-007bbc34) 範囲 `[['007bbc34', '007bbc4b']]`
  - `CONDITIONAL_JUMP` [`007bbc48`](#insn-007bbc48) → [`007bbc58`](#insn-007bbc58)
  - `FALL_THROUGH` [`007bbc48`](#insn-007bbc48) → [`007bbc4c`](#insn-007bbc4c)
- ブロック [`007bbc4c`](#insn-007bbc4c) 範囲 `[['007bbc4c', '007bbc57']]`
  - `CONDITIONAL_JUMP` [`007bbc54`](#insn-007bbc54) → [`007bbc68`](#insn-007bbc68)
  - `FALL_THROUGH` [`007bbc54`](#insn-007bbc54) → [`007bbc58`](#insn-007bbc58)
- ブロック [`007bbc58`](#insn-007bbc58) 範囲 `[['007bbc58', '007bbc5b']]`
  - `FALL_THROUGH` [`007bbc58`](#insn-007bbc58) → [`007bbc5c`](#insn-007bbc5c)
- ブロック [`007bbc5c`](#insn-007bbc5c) 範囲 `[['007bbc5c', '007bbc67']]`
- ブロック [`007bbc68`](#insn-007bbc68) 範囲 `[['007bbc68', '007bbc6f']]`
  - `UNCONDITIONAL_JUMP` [`007bbc6c`](#insn-007bbc6c) → [`007bbc5c`](#insn-007bbc5c)

## 命令位置別の参照

- [`007bbbec`](#insn-007bbbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbbf0`](#insn-007bbbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbbfc`](#insn-007bbbfc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`007bbc08`](#insn-007bbc08) → `0038f284`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[15]`
- [`007bbc0c`](#insn-007bbc0c) → [`0080018c`](../00800/0080018c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080018c` · 推定シンボル `None` · 推定型 `None`
- [`007bbc10`](#insn-007bbc10) → [`007bbc58`](#insn-007bbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc1c`](#insn-007bbc1c) → `00344440`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`007bbc24`](#insn-007bbc24) → [`007bbc58`](#insn-007bbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc28`](#insn-007bbc28) → [`00802ea0`](../00802/00802ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802ea0` · 推定シンボル `None` · 推定型 `None`
- [`007bbc30`](#insn-007bbc30) → [`007bbc58`](#insn-007bbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc44`](#insn-007bbc44) → [`008077b8`](../00807/008077b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008077b8` · 推定シンボル `None` · 推定型 `None`
- [`007bbc48`](#insn-007bbc48) → [`007bbc58`](#insn-007bbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc54`](#insn-007bbc54) → [`007bbc68`](#insn-007bbc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc5c`](#insn-007bbc5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc60`](#insn-007bbc60) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bbc6c`](#insn-007bbc6c) → [`007bbc5c`](#insn-007bbc5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007bbbec`](#insn-007bbbec)

~~~json
{
  "source": "007bbbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbbf0`](#insn-007bbbf0)

~~~json
{
  "source": "007bbbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbbfc`](#insn-007bbbfc)

~~~json
{
  "source": "007bbbfc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bbc08`](#insn-007bbc08)

~~~json
{
  "source": "007bbc08",
  "target": "0038f284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038f27d",
  "offset": 7,
  "size": 15,
  "datatype": "byte[15]",
  "bytes": "02400e10440c1d109e029d04000000",
  "capture_start": "0038f27d",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bbc0c`](#insn-007bbc0c)

~~~json
{
  "source": "007bbc0c",
  "target": "0080018c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bbc10`](#insn-007bbc10)

~~~json
{
  "source": "007bbc10",
  "target": "007bbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc1c`](#insn-007bbc1c)

~~~json
{
  "source": "007bbc1c",
  "target": "00344440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344440",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "00344440",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bbc24`](#insn-007bbc24)

~~~json
{
  "source": "007bbc24",
  "target": "007bbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc28`](#insn-007bbc28)

~~~json
{
  "source": "007bbc28",
  "target": "00802ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bbc30`](#insn-007bbc30)

~~~json
{
  "source": "007bbc30",
  "target": "007bbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc44`](#insn-007bbc44)

~~~json
{
  "source": "007bbc44",
  "target": "008077b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007bbc48`](#insn-007bbc48)

~~~json
{
  "source": "007bbc48",
  "target": "007bbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc54`](#insn-007bbc54)

~~~json
{
  "source": "007bbc54",
  "target": "007bbc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc5c`](#insn-007bbc5c)

~~~json
{
  "source": "007bbc5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc60`](#insn-007bbc60)

~~~json
{
  "source": "007bbc60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bbc6c`](#insn-007bbc6c)

~~~json
{
  "source": "007bbc6c",
  "target": "007bbc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
