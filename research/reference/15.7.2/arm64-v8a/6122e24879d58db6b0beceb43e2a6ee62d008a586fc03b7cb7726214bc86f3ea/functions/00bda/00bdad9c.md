# 00bdad9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae54.md) · 移動量 `+0xb8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0005.md#compare-0ea573bb0ecb21d46a597654f2d5ee44)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdad9c",
  "name": "_Znwm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e0d097a891612fbe969d9e379d8f12c24a4775fa996941e7029ddb6caecc5b6",
  "source_text_sha256": "6e0d097a891612fbe969d9e379d8f12c24a4775fa996941e7029ddb6caecc5b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdad9c",
        "00bdae07"
      ]
    ],
    "bytes_sha256": "5a1b83c409fbd184735300757d8d136347cec4dc26c1e1b1fdc13942896d57ab",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bdaf40](../00bda/00bdaf40.md)

## 呼び出し先

- [00bdafa0](../00bda/00bdafa0.md)
- [00bdafc0](../00bda/00bdafc0.md)
- [00bdbaf0](../00bdb/00bdbaf0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00be1d20](../00be1/00be1d20.md)

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
      return;
    }
    pcVar2 = (code *)_ZSt15get_new_handlerv();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
                    /* try { // try from 00bdadcc to 00cdadf3 has its CatchHandler @ 00bdadcc
                       catch() { ... } // from try @ 00bdadcc with catch @ 00bdadcc
                       catch() { ... } // from try @ 00bdae2c with catch @ 00bdadcc */
  }
  uVar3 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* try { // try from 00bdadf4 to 00cdae2b has its CatchHandler @ 00bdae5c */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar3,PTR__ZTISt9bad_alloc_00c1aef8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1af00);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdad9c"></a> `00bdad9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdada0"></a> `00bdada0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdada4"></a> `00bdada4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdada8"></a> `00bdada8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bdadac"></a> `00bdadac` | `1f 04 00 f1` | cmp x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdadb0"></a> `00bdadb0` | `13 84 9f 9a` | csinc x19,x0,xzr,hi | `FALL_THROUGH`
<a id="insn-00bdadb4"></a> `00bdadb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdadb8"></a> `00bdadb8` | `c6 08 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadbc"></a> `00bdadbc` | `a0 00 00 b5` | cbnz x0,0x00bdadd0 | `CONDITIONAL_JUMP`
<a id="insn-00bdadc0"></a> `00bdadc0` | `d8 1b 00 94` | bl 0x00be1d20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadc4"></a> `00bdadc4` | `e0 00 00 b4` | cbz x0,0x00bdade0 | `CONDITIONAL_JUMP`
<a id="insn-00bdadc8"></a> `00bdadc8` | `00 00 3f d6` | blr x0 | `COMPUTED_CALL`
<a id="insn-00bdadcc"></a> `00bdadcc` | `fa ff ff 17` | b 0x00bdadb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdadd0"></a> `00bdadd0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdadd4"></a> `00bdadd4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdadd8"></a> `00bdadd8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdaddc"></a> `00bdaddc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdade0"></a> `00bdade0` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdade4"></a> `00bdade4` | `6f 00 00 94` | bl 0x00bdafa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdade8"></a> `00bdade8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdadec"></a> `00bdadec` | `41 03 00 94` | bl 0x00bdbaf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadf0"></a> `00bdadf0` | `01 02 00 90` | adrp x1,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bdadf4"></a> `00bdadf4` | `02 02 00 90` | adrp x2,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bdadf8"></a> `00bdadf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdadfc"></a> `00bdadfc` | `21 7c 47 f9` | ldr x1,[x1, #0xef8] | `FALL_THROUGH`
<a id="insn-00bdae00"></a> `00bdae00` | `42 80 47 f9` | ldr x2,[x2, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdae04"></a> `00bdae04` | `6f 00 00 94` | bl 0x00bdafc0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdad9c`](#insn-00bdad9c) 範囲 `[['00bdad9c', '00bdadb3']]`
  - `FALL_THROUGH` [`00bdadb0`](#insn-00bdadb0) → [`00bdadb4`](#insn-00bdadb4)
- ブロック [`00bdadb4`](#insn-00bdadb4) 範囲 `[['00bdadb4', '00bdadbf']]`
  - `CONDITIONAL_JUMP` [`00bdadbc`](#insn-00bdadbc) → [`00bdadd0`](#insn-00bdadd0)
  - `FALL_THROUGH` [`00bdadbc`](#insn-00bdadbc) → [`00bdadc0`](#insn-00bdadc0)
- ブロック [`00bdadc0`](#insn-00bdadc0) 範囲 `[['00bdadc0', '00bdadc7']]`
  - `CONDITIONAL_JUMP` [`00bdadc4`](#insn-00bdadc4) → [`00bdade0`](#insn-00bdade0)
  - `FALL_THROUGH` [`00bdadc4`](#insn-00bdadc4) → [`00bdadc8`](#insn-00bdadc8)
- ブロック [`00bdadc8`](#insn-00bdadc8) 範囲 `[['00bdadc8', '00bdadcb']]`
  - `FALL_THROUGH` [`00bdadc8`](#insn-00bdadc8) → [`00bdadcc`](#insn-00bdadcc)
- ブロック [`00bdadcc`](#insn-00bdadcc) 範囲 `[['00bdadcc', '00bdadcf']]`
  - `UNCONDITIONAL_JUMP` [`00bdadcc`](#insn-00bdadcc) → [`00bdadb4`](#insn-00bdadb4)
- ブロック [`00bdadd0`](#insn-00bdadd0) 範囲 `[['00bdadd0', '00bdaddf']]`
- ブロック [`00bdade0`](#insn-00bdade0) 範囲 `[['00bdade0', '00bdadf3']]`
  - `FALL_THROUGH` [`00bdadf0`](#insn-00bdadf0) → [`00bdadf4`](#insn-00bdadf4)
- ブロック [`00bdadf4`](#insn-00bdadf4) 範囲 `[['00bdadf4', '00bdae07']]`

## 命令位置別の参照

- [`00bdada0`](#insn-00bdada0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdada4`](#insn-00bdada4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadb8`](#insn-00bdadb8) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdadbc`](#insn-00bdadbc) → [`00bdadd0`](#insn-00bdadd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadc0`](#insn-00bdadc0) → [`00be1d20`](../00be1/00be1d20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1d20` · 推定シンボル `None` · 推定型 `None`
- [`00bdadc4`](#insn-00bdadc4) → [`00bdade0`](#insn-00bdade0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadcc`](#insn-00bdadcc) → [`00bdadb4`](#insn-00bdadb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadd0`](#insn-00bdadd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadd4`](#insn-00bdadd4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdade4`](#insn-00bdade4) → [`00bdafa0`](00bdafa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafa0` · 推定シンボル `None` · 推定型 `None`
- [`00bdadec`](#insn-00bdadec) → [`00bdbaf0`](../00bdb/00bdbaf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbaf0` · 推定シンボル `None` · 推定型 `None`
- [`00bdadfc`](#insn-00bdadfc) → `00c1aef8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdadfc`](#insn-00bdadfc) → `00c167f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`00bdae00`](#insn-00bdae00) → `00c1af00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdae00`](#insn-00bdae00) → [`00bbac28`](../00bba/00bbac28.md) · `PARAM` · `ANALYSIS` · 関数 `00bbac28` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`00bdae04`](#insn-00bdae04) → [`00bdafc0`](00bdafc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafc0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdada0`](#insn-00bdada0)

~~~json
{
  "source": "00bdada0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdada4`](#insn-00bdada4)

~~~json
{
  "source": "00bdada4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadb8`](#insn-00bdadb8)

~~~json
{
  "source": "00bdadb8",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadbc`](#insn-00bdadbc)

~~~json
{
  "source": "00bdadbc",
  "target": "00bdadd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadc0`](#insn-00bdadc0)

~~~json
{
  "source": "00bdadc0",
  "target": "00be1d20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadc4`](#insn-00bdadc4)

~~~json
{
  "source": "00bdadc4",
  "target": "00bdade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadcc`](#insn-00bdadcc)

~~~json
{
  "source": "00bdadcc",
  "target": "00bdadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadd0`](#insn-00bdadd0)

~~~json
{
  "source": "00bdadd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadd4`](#insn-00bdadd4)

~~~json
{
  "source": "00bdadd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdade4`](#insn-00bdade4)

~~~json
{
  "source": "00bdade4",
  "target": "00bdafa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadec`](#insn-00bdadec)

~~~json
{
  "source": "00bdadec",
  "target": "00bdbaf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadfc`](#insn-00bdadfc)

~~~json
{
  "source": "00bdadfc",
  "target": "00c1aef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1aef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdadfc`](#insn-00bdadfc)

~~~json
{
  "source": "00bdadfc",
  "target": "00c167f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c167f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdae00`](#insn-00bdae00)

~~~json
{
  "source": "00bdae00",
  "target": "00c1af00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1af00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdae00`](#insn-00bdae00)

~~~json
{
  "source": "00bdae00",
  "target": "00bbac28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae04`](#insn-00bdae04)

~~~json
{
  "source": "00bdae04",
  "target": "00bdafc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
