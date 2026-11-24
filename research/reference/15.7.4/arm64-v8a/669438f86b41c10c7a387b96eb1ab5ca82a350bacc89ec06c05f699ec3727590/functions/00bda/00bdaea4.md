# 00bdaea4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae54.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-62385817288227516366d687b46ba813)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c578ec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-3d49dbbea2512dbb136aeaa218db3371)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaea4",
  "name": "_Znwm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c",
  "source_text_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaea4",
        "00bdaf0f"
      ]
    ],
    "bytes_sha256": "4494219ea12558f2d9ee4e6c8e52ad0fbfa77d8b8aee15e4a8c7a9fc968d6070",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bdb040](../00bdb/00bdb040.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdbbf0](../00bdb/00bdbbf0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00be1e20](../00be1/00be1e20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 923 bytes

~~~c

void _Znwm(size_t param_1)

{
  void *pvVar1;
  code *pcVar2;
  undefined8 uVar3;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  while( true ) {
    pvVar1 = malloc(param_1);
    if (pvVar1 != (void *)0x0) {
                    /* try { // try from 00bdaed8 to 00cdaeff has its CatchHandler @ 00bdaed8
                       catch() { ... } // from try @ 00bdaed8 with catch @ 00bdaed8
                       catch() { ... } // from try @ 00bdaf38 with catch @ 00bdaed8 */
      return;
    }
    pcVar2 = (code *)_ZSt15get_new_handlerv();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
  }
  uVar3 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* try { // try from 00bdaf00 to 00cdaf37 has its CatchHandler @ 00bdaf68 */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar3,PTR__ZTISt9bad_alloc_00c1aff8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1b000);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaea4"></a> `00bdaea4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdaea8"></a> `00bdaea8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdaeac"></a> `00bdaeac` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaeb0"></a> `00bdaeb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bdaeb4"></a> `00bdaeb4` | `1f 04 00 f1` | cmp x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaeb8"></a> `00bdaeb8` | `13 84 9f 9a` | csinc x19,x0,xzr,hi | `FALL_THROUGH`
<a id="insn-00bdaebc"></a> `00bdaebc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdaec0"></a> `00bdaec0` | `c4 08 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaec4"></a> `00bdaec4` | `a0 00 00 b5` | cbnz x0,0x00bdaed8 | `CONDITIONAL_JUMP`
<a id="insn-00bdaec8"></a> `00bdaec8` | `d6 1b 00 94` | bl 0x00be1e20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaecc"></a> `00bdaecc` | `e0 00 00 b4` | cbz x0,0x00bdaee8 | `CONDITIONAL_JUMP`
<a id="insn-00bdaed0"></a> `00bdaed0` | `00 00 3f d6` | blr x0 | `COMPUTED_CALL`
<a id="insn-00bdaed4"></a> `00bdaed4` | `fa ff ff 17` | b 0x00bdaebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdaed8"></a> `00bdaed8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaedc"></a> `00bdaedc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdaee0"></a> `00bdaee0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdaee4"></a> `00bdaee4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdaee8"></a> `00bdaee8` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaeec"></a> `00bdaeec` | `6d 00 00 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaef0"></a> `00bdaef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdaef4"></a> `00bdaef4` | `3f 03 00 94` | bl 0x00bdbbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaef8"></a> `00bdaef8` | `01 02 00 90` | adrp x1,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bdaefc"></a> `00bdaefc` | `02 02 00 b0` | adrp x2,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdaf00"></a> `00bdaf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdaf04"></a> `00bdaf04` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bdaf08"></a> `00bdaf08` | `42 00 40 f9` | ldr x2,[x2] | `FALL_THROUGH`
<a id="insn-00bdaf0c"></a> `00bdaf0c` | `6d 00 00 94` | bl 0x00bdb0c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaea4`](#insn-00bdaea4) 範囲 `[['00bdaea4', '00bdaebb']]`
  - `FALL_THROUGH` [`00bdaeb8`](#insn-00bdaeb8) → [`00bdaebc`](#insn-00bdaebc)
- ブロック [`00bdaebc`](#insn-00bdaebc) 範囲 `[['00bdaebc', '00bdaec7']]`
  - `CONDITIONAL_JUMP` [`00bdaec4`](#insn-00bdaec4) → [`00bdaed8`](#insn-00bdaed8)
  - `FALL_THROUGH` [`00bdaec4`](#insn-00bdaec4) → [`00bdaec8`](#insn-00bdaec8)
- ブロック [`00bdaec8`](#insn-00bdaec8) 範囲 `[['00bdaec8', '00bdaecf']]`
  - `CONDITIONAL_JUMP` [`00bdaecc`](#insn-00bdaecc) → [`00bdaee8`](#insn-00bdaee8)
  - `FALL_THROUGH` [`00bdaecc`](#insn-00bdaecc) → [`00bdaed0`](#insn-00bdaed0)
- ブロック [`00bdaed0`](#insn-00bdaed0) 範囲 `[['00bdaed0', '00bdaed7']]`
  - `UNCONDITIONAL_JUMP` [`00bdaed4`](#insn-00bdaed4) → [`00bdaebc`](#insn-00bdaebc)
- ブロック [`00bdaed8`](#insn-00bdaed8) 範囲 `[['00bdaed8', '00bdaee7']]`
- ブロック [`00bdaee8`](#insn-00bdaee8) 範囲 `[['00bdaee8', '00bdaeff']]`
  - `FALL_THROUGH` [`00bdaefc`](#insn-00bdaefc) → [`00bdaf00`](#insn-00bdaf00)
- ブロック [`00bdaf00`](#insn-00bdaf00) 範囲 `[['00bdaf00', '00bdaf0f']]`

## 命令位置別の参照

- [`00bdaea8`](#insn-00bdaea8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaeac`](#insn-00bdaeac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaec0`](#insn-00bdaec0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaec4`](#insn-00bdaec4) → [`00bdaed8`](#insn-00bdaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaec8`](#insn-00bdaec8) → [`00be1e20`](../00be1/00be1e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e20` · 推定シンボル `None` · 推定型 `None`
- [`00bdaecc`](#insn-00bdaecc) → [`00bdaee8`](#insn-00bdaee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaed4`](#insn-00bdaed4) → [`00bdaebc`](#insn-00bdaebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaed8`](#insn-00bdaed8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaedc`](#insn-00bdaedc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaeec`](#insn-00bdaeec) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaef4`](#insn-00bdaef4) → [`00bdbbf0`](../00bdb/00bdbbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbbf0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf04`](#insn-00bdaf04) → `00c1aff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaf04`](#insn-00bdaf04) → `00c168f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`00bdaf08`](#insn-00bdaf08) → `00c1b000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaf08`](#insn-00bdaf08) → [`00bbad34`](../00bba/00bbad34.md) · `PARAM` · `ANALYSIS` · 関数 `00bbad34` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`00bdaf0c`](#insn-00bdaf0c) → [`00bdb0c0`](../00bdb/00bdb0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaea8`](#insn-00bdaea8)

~~~json
{
  "source": "00bdaea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaeac`](#insn-00bdaeac)

~~~json
{
  "source": "00bdaeac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaec0`](#insn-00bdaec0)

~~~json
{
  "source": "00bdaec0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaec4`](#insn-00bdaec4)

~~~json
{
  "source": "00bdaec4",
  "target": "00bdaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaec8`](#insn-00bdaec8)

~~~json
{
  "source": "00bdaec8",
  "target": "00be1e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaecc`](#insn-00bdaecc)

~~~json
{
  "source": "00bdaecc",
  "target": "00bdaee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaed4`](#insn-00bdaed4)

~~~json
{
  "source": "00bdaed4",
  "target": "00bdaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaed8`](#insn-00bdaed8)

~~~json
{
  "source": "00bdaed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaedc`](#insn-00bdaedc)

~~~json
{
  "source": "00bdaedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaeec`](#insn-00bdaeec)

~~~json
{
  "source": "00bdaeec",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaef4`](#insn-00bdaef4)

~~~json
{
  "source": "00bdaef4",
  "target": "00bdbbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf04`](#insn-00bdaf04)

~~~json
{
  "source": "00bdaf04",
  "target": "00c1aff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1aff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf04`](#insn-00bdaf04)

~~~json
{
  "source": "00bdaf04",
  "target": "00c168f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c168f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf08`](#insn-00bdaf08)

~~~json
{
  "source": "00bdaf08",
  "target": "00c1b000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf08`](#insn-00bdaf08)

~~~json
{
  "source": "00bdaf08",
  "target": "00bbad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf0c`](#insn-00bdaf0c)

~~~json
{
  "source": "00bdaf0c",
  "target": "00bdb0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
