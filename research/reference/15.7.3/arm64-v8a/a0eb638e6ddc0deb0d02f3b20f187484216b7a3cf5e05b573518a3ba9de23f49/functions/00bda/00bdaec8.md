# 00bdaec8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdae10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md) · 移動量 `+0xb8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-2effd8f32a4890254855832e6ece5383)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdaf18`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-ed42dd44f451501dc4c6682e6875ba25)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaec8",
  "name": "_ZnwmSt11align_val_t",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f264c902acdd2565ceb5fc7994a0782381d572ab27fdf26feeb62121fb13c26f",
  "source_text_sha256": "f264c902acdd2565ceb5fc7994a0782381d572ab27fdf26feeb62121fb13c26f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaec8",
        "00bdaf57"
      ]
    ],
    "bytes_sha256": "8867a27d18820425dc5931814140113044afdb799525977f9d633ff94259b41e",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00be1eb0](../00be1/00be1eb0.md)

## 呼び出し先

- [00bdb050](../00bdb/00bdb050.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdbba0](../00bdb/00bdbba0.md)
- [00be1dd0](../00be1/00be1dd0.md)
- [00be1ec0](../00be1/00be1ec0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1131 bytes

~~~c

void _ZnwmSt11align_val_t(size_t param_1,size_t param_2)

{
  code *pcVar1;
  undefined8 uVar2;
  void *local_28;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  if (param_2 < 9) {
    param_2 = 8;
  }
  while( true ) {
                    /* try { // try from 00bdaef4 to 00cdaf53 has its CatchHandler @ 00bdae94 */
    local_28 = (void *)0x0;
    posix_memalign(&local_28,param_2,param_1);
    if (local_28 != (void *)0x0) {
                    /* catch() { ... } // from try @ 00bdaebc with catch @ 00bdaf24 */
      return;
    }
    pcVar1 = (code *)_ZSt15get_new_handlerv();
    if (pcVar1 == (code *)0x0) break;
    (*pcVar1)();
  }
  uVar2 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bdaf54 to 00cdaf7b has its CatchHandler @ 00bdaf54
                       catch() { ... } // from try @ 00bdaf54 with catch @ 00bdaf54
                       catch() { ... } // from try @ 00bdafb4 with catch @ 00bdaf54 */
  __cxa_throw(uVar2,PTR__ZTISt9bad_alloc_00c1afa8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1afb0);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaec8"></a> `00bdaec8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdaecc"></a> `00bdaecc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdaed0"></a> `00bdaed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaed4"></a> `00bdaed4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaed8"></a> `00bdaed8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdaedc"></a> `00bdaedc` | `1f 04 00 f1` | cmp x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaee0"></a> `00bdaee0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaee4"></a> `00bdaee4` | `13 84 9f 9a` | csinc x19,x0,xzr,hi | `FALL_THROUGH`
<a id="insn-00bdaee8"></a> `00bdaee8` | `3f 20 00 f1` | cmp x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaeec"></a> `00bdaeec` | `34 80 88 9a` | csel x20,x1,x8,hi | `FALL_THROUGH`
<a id="insn-00bdaef0"></a> `00bdaef0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaef4"></a> `00bdaef4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdaef8"></a> `00bdaef8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bdaefc"></a> `00bdaefc` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaf00"></a> `00bdaf00` | `f0 1b 00 94` | bl 0x00be1ec0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaf04"></a> `00bdaf04` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaf08"></a> `00bdaf08` | `a0 00 00 b5` | cbnz x0,0x00bdaf1c | `CONDITIONAL_JUMP`
<a id="insn-00bdaf0c"></a> `00bdaf0c` | `b1 1b 00 94` | bl 0x00be1dd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaf10"></a> `00bdaf10` | `00 01 00 b4` | cbz x0,0x00bdaf30 | `CONDITIONAL_JUMP`
<a id="insn-00bdaf14"></a> `00bdaf14` | `00 00 3f d6` | blr x0 | `COMPUTED_CALL`
<a id="insn-00bdaf18"></a> `00bdaf18` | `f6 ff ff 17` | b 0x00bdaef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdaf1c"></a> `00bdaf1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaf20"></a> `00bdaf20` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaf24"></a> `00bdaf24` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdaf28"></a> `00bdaf28` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdaf2c"></a> `00bdaf2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdaf30"></a> `00bdaf30` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaf34"></a> `00bdaf34` | `47 00 00 94` | bl 0x00bdb050 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaf38"></a> `00bdaf38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdaf3c"></a> `00bdaf3c` | `19 03 00 94` | bl 0x00bdbba0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaf40"></a> `00bdaf40` | `01 02 00 90` | adrp x1,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bdaf44"></a> `00bdaf44` | `02 02 00 90` | adrp x2,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bdaf48"></a> `00bdaf48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdaf4c"></a> `00bdaf4c` | `21 d4 47 f9` | ldr x1,[x1, #0xfa8] | `FALL_THROUGH`
<a id="insn-00bdaf50"></a> `00bdaf50` | `42 d8 47 f9` | ldr x2,[x2, #0xfb0] | `FALL_THROUGH`
<a id="insn-00bdaf54"></a> `00bdaf54` | `47 00 00 94` | bl 0x00bdb070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaec8`](#insn-00bdaec8) 範囲 `[['00bdaec8', '00bdaeef']]`
  - `FALL_THROUGH` [`00bdaeec`](#insn-00bdaeec) → [`00bdaef0`](#insn-00bdaef0)
- ブロック [`00bdaef0`](#insn-00bdaef0) 範囲 `[['00bdaef0', '00bdaef3']]`
  - `FALL_THROUGH` [`00bdaef0`](#insn-00bdaef0) → [`00bdaef4`](#insn-00bdaef4)
- ブロック [`00bdaef4`](#insn-00bdaef4) 範囲 `[['00bdaef4', '00bdaf0b']]`
  - `CONDITIONAL_JUMP` [`00bdaf08`](#insn-00bdaf08) → [`00bdaf1c`](#insn-00bdaf1c)
  - `FALL_THROUGH` [`00bdaf08`](#insn-00bdaf08) → [`00bdaf0c`](#insn-00bdaf0c)
- ブロック [`00bdaf0c`](#insn-00bdaf0c) 範囲 `[['00bdaf0c', '00bdaf13']]`
  - `CONDITIONAL_JUMP` [`00bdaf10`](#insn-00bdaf10) → [`00bdaf30`](#insn-00bdaf30)
  - `FALL_THROUGH` [`00bdaf10`](#insn-00bdaf10) → [`00bdaf14`](#insn-00bdaf14)
- ブロック [`00bdaf14`](#insn-00bdaf14) 範囲 `[['00bdaf14', '00bdaf1b']]`
  - `UNCONDITIONAL_JUMP` [`00bdaf18`](#insn-00bdaf18) → [`00bdaef0`](#insn-00bdaef0)
- ブロック [`00bdaf1c`](#insn-00bdaf1c) 範囲 `[['00bdaf1c', '00bdaf23']]`
  - `FALL_THROUGH` [`00bdaf20`](#insn-00bdaf20) → [`00bdaf24`](#insn-00bdaf24)
- ブロック [`00bdaf24`](#insn-00bdaf24) 範囲 `[['00bdaf24', '00bdaf2f']]`
- ブロック [`00bdaf30`](#insn-00bdaf30) 範囲 `[['00bdaf30', '00bdaf53']]`
  - `FALL_THROUGH` [`00bdaf50`](#insn-00bdaf50) → [`00bdaf54`](#insn-00bdaf54)
- ブロック [`00bdaf54`](#insn-00bdaf54) 範囲 `[['00bdaf54', '00bdaf57']]`

## 命令位置別の参照

- [`00bdaed0`](#insn-00bdaed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaed4`](#insn-00bdaed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaefc`](#insn-00bdaefc) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf00`](#insn-00bdaf00) → [`00be1ec0`](../00be1/00be1ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ec0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf04`](#insn-00bdaf04) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf08`](#insn-00bdaf08) → [`00bdaf1c`](#insn-00bdaf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf0c`](#insn-00bdaf0c) → [`00be1dd0`](../00be1/00be1dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1dd0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf10`](#insn-00bdaf10) → [`00bdaf30`](#insn-00bdaf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf18`](#insn-00bdaf18) → [`00bdaef0`](#insn-00bdaef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf1c`](#insn-00bdaf1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf20`](#insn-00bdaf20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf34`](#insn-00bdaf34) → [`00bdb050`](../00bdb/00bdb050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb050` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf3c`](#insn-00bdaf3c) → [`00bdbba0`](../00bdb/00bdbba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbba0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf4c`](#insn-00bdaf4c) → `00c1afa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaf4c`](#insn-00bdaf4c) → `00c168a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`00bdaf50`](#insn-00bdaf50) → `00c1afb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaf50`](#insn-00bdaf50) → [`00bbacf0`](../00bba/00bbacf0.md) · `PARAM` · `ANALYSIS` · 関数 `00bbacf0` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`00bdaf54`](#insn-00bdaf54) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaed0`](#insn-00bdaed0)

~~~json
{
  "source": "00bdaed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaed4`](#insn-00bdaed4)

~~~json
{
  "source": "00bdaed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaefc`](#insn-00bdaefc)

~~~json
{
  "source": "00bdaefc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf00`](#insn-00bdaf00)

~~~json
{
  "source": "00bdaf00",
  "target": "00be1ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf04`](#insn-00bdaf04)

~~~json
{
  "source": "00bdaf04",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf08`](#insn-00bdaf08)

~~~json
{
  "source": "00bdaf08",
  "target": "00bdaf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf0c`](#insn-00bdaf0c)

~~~json
{
  "source": "00bdaf0c",
  "target": "00be1dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf10`](#insn-00bdaf10)

~~~json
{
  "source": "00bdaf10",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf18`](#insn-00bdaf18)

~~~json
{
  "source": "00bdaf18",
  "target": "00bdaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf1c`](#insn-00bdaf1c)

~~~json
{
  "source": "00bdaf1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf20`](#insn-00bdaf20)

~~~json
{
  "source": "00bdaf20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf34`](#insn-00bdaf34)

~~~json
{
  "source": "00bdaf34",
  "target": "00bdb050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf3c`](#insn-00bdaf3c)

~~~json
{
  "source": "00bdaf3c",
  "target": "00bdbba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf4c`](#insn-00bdaf4c)

~~~json
{
  "source": "00bdaf4c",
  "target": "00c1afa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1afa8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf4c`](#insn-00bdaf4c)

~~~json
{
  "source": "00bdaf4c",
  "target": "00c168a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c168a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf50`](#insn-00bdaf50)

~~~json
{
  "source": "00bdaf50",
  "target": "00c1afb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1afb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaf50`](#insn-00bdaf50)

~~~json
{
  "source": "00bdaf50",
  "target": "00bbacf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf54`](#insn-00bdaf54)

~~~json
{
  "source": "00bdaf54",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
