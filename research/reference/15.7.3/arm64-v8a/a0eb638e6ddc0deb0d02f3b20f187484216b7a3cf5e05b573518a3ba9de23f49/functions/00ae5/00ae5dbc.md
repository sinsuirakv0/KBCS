# 00ae5dbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae5cf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5cf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0058.md#compare-ce028f3a05ec049e525b21a3ed692948)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae5e00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-1cb96fcdcb1e027857aeff328eb7fd81)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae5dbc",
  "name": "_ZN8firebase4util3log12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f179d79431745754eaadfe5cd77fe8b81e06911a0ae90f354c3162a0b500948",
  "source_text_sha256": "4f179d79431745754eaadfe5cd77fe8b81e06911a0ae90f354c3162a0b500948",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae5dbc",
        "00ae5e5b"
      ]
    ],
    "bytes_sha256": "c5c4a5524394df1a355fcf71632a8f3bca2c21314000d1dd5998b4775cfad413",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 697 bytes

~~~c

void _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a03d8 != 0) {
                    /* try { // try from 00ae5de4 to 00be5deb has its CatchHandler @ 00ae5ee4 */
    if (DAT_010a03e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a03e0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a03d8);
    DAT_010a03d8 = 0;
  }
                    /* try { // try from 00ae5e58 to 00be5e5f has its CatchHandler @ 00ae5ee8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae5dbc"></a> `00ae5dbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae5dc0"></a> `00ae5dc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae5dc4"></a> `00ae5dc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae5dc8"></a> `00ae5dc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae5dcc"></a> `00ae5dcc` | `d4 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae5dd0"></a> `00ae5dd0` | `81 ee 41 f9` | ldr x1,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00ae5dd4"></a> `00ae5dd4` | `c1 03 00 b4` | cbz x1,0x00ae5e4c | `CONDITIONAL_JUMP`
<a id="insn-00ae5dd8"></a> `00ae5dd8` | `d5 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae5ddc"></a> `00ae5ddc` | `a8 82 4f 39` | ldrb w8,[x21, #0x3e0] | `FALL_THROUGH`
<a id="insn-00ae5de0"></a> `00ae5de0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae5de4"></a> `00ae5de4` | `c8 00 00 34` | cbz w8,0x00ae5dfc | `CONDITIONAL_JUMP`
<a id="insn-00ae5de8"></a> `00ae5de8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae5dec"></a> `00ae5dec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae5df0"></a> `00ae5df0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00ae5df4"></a> `00ae5df4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae5df8"></a> `00ae5df8` | `bf 82 0f 39` | strb wzr,[x21, #0x3e0] | `FALL_THROUGH`
<a id="insn-00ae5dfc"></a> `00ae5dfc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae5e00"></a> `00ae5e00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae5e04"></a> `00ae5e04` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00ae5e08"></a> `00ae5e08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae5e0c"></a> `00ae5e0c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00ae5e10"></a> `00ae5e10` | `20 01 00 54` | b.eq 0x00ae5e34 | `CONDITIONAL_JUMP`
<a id="insn-00ae5e14"></a> `00ae5e14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae5e18"></a> `00ae5e18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae5e1c"></a> `00ae5e1c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00ae5e20"></a> `00ae5e20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae5e24"></a> `00ae5e24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae5e28"></a> `00ae5e28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae5e2c"></a> `00ae5e2c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00ae5e30"></a> `00ae5e30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae5e34"></a> `00ae5e34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae5e38"></a> `00ae5e38` | `81 ee 41 f9` | ldr x1,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00ae5e3c"></a> `00ae5e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae5e40"></a> `00ae5e40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae5e44"></a> `00ae5e44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae5e48"></a> `00ae5e48` | `9f ee 01 f9` | str xzr,[x20, #0x3d8] | `FALL_THROUGH`
<a id="insn-00ae5e4c"></a> `00ae5e4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae5e50"></a> `00ae5e50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae5e54"></a> `00ae5e54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae5e58"></a> `00ae5e58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae5dbc`](#insn-00ae5dbc) 範囲 `[['00ae5dbc', '00ae5dd7']]`
  - `CONDITIONAL_JUMP` [`00ae5dd4`](#insn-00ae5dd4) → [`00ae5e4c`](#insn-00ae5e4c)
  - `FALL_THROUGH` [`00ae5dd4`](#insn-00ae5dd4) → [`00ae5dd8`](#insn-00ae5dd8)
- ブロック [`00ae5dd8`](#insn-00ae5dd8) 範囲 `[['00ae5dd8', '00ae5de3']]`
  - `FALL_THROUGH` [`00ae5de0`](#insn-00ae5de0) → [`00ae5de4`](#insn-00ae5de4)
- ブロック [`00ae5de4`](#insn-00ae5de4) 範囲 `[['00ae5de4', '00ae5de7']]`
  - `CONDITIONAL_JUMP` [`00ae5de4`](#insn-00ae5de4) → [`00ae5dfc`](#insn-00ae5dfc)
  - `FALL_THROUGH` [`00ae5de4`](#insn-00ae5de4) → [`00ae5de8`](#insn-00ae5de8)
- ブロック [`00ae5de8`](#insn-00ae5de8) 範囲 `[['00ae5de8', '00ae5dfb']]`
  - `FALL_THROUGH` [`00ae5df8`](#insn-00ae5df8) → [`00ae5dfc`](#insn-00ae5dfc)
- ブロック [`00ae5dfc`](#insn-00ae5dfc) 範囲 `[['00ae5dfc', '00ae5e13']]`
  - `CONDITIONAL_JUMP` [`00ae5e10`](#insn-00ae5e10) → [`00ae5e34`](#insn-00ae5e34)
  - `FALL_THROUGH` [`00ae5e10`](#insn-00ae5e10) → [`00ae5e14`](#insn-00ae5e14)
- ブロック [`00ae5e14`](#insn-00ae5e14) 範囲 `[['00ae5e14', '00ae5e33']]`
  - `FALL_THROUGH` [`00ae5e30`](#insn-00ae5e30) → [`00ae5e34`](#insn-00ae5e34)
- ブロック [`00ae5e34`](#insn-00ae5e34) 範囲 `[['00ae5e34', '00ae5e4b']]`
  - `FALL_THROUGH` [`00ae5e48`](#insn-00ae5e48) → [`00ae5e4c`](#insn-00ae5e4c)
- ブロック [`00ae5e4c`](#insn-00ae5e4c) 範囲 `[['00ae5e4c', '00ae5e57']]`
  - `FALL_THROUGH` [`00ae5e54`](#insn-00ae5e54) → [`00ae5e58`](#insn-00ae5e58)
- ブロック [`00ae5e58`](#insn-00ae5e58) 範囲 `[['00ae5e58', '00ae5e5b']]`

## 命令位置別の参照

- [`00ae5dbc`](#insn-00ae5dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5dc0`](#insn-00ae5dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5dc4`](#insn-00ae5dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5dd0`](#insn-00ae5dd0) → `010a03d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae5dd4`](#insn-00ae5dd4) → [`00ae5e4c`](#insn-00ae5e4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5ddc`](#insn-00ae5ddc) → `010a03e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae5de4`](#insn-00ae5de4) → [`00ae5dfc`](#insn-00ae5dfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5df8`](#insn-00ae5df8) → `010a03e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae5e10`](#insn-00ae5e10) → [`00ae5e34`](#insn-00ae5e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5e38`](#insn-00ae5e38) → `010a03d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae5e48`](#insn-00ae5e48) → `010a03d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae5e4c`](#insn-00ae5e4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5e50`](#insn-00ae5e50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae5dbc`](#insn-00ae5dbc)

~~~json
{
  "source": "00ae5dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5dc0`](#insn-00ae5dc0)

~~~json
{
  "source": "00ae5dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5dc4`](#insn-00ae5dc4)

~~~json
{
  "source": "00ae5dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5dd0`](#insn-00ae5dd0)

~~~json
{
  "source": "00ae5dd0",
  "target": "010a03d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5dd4`](#insn-00ae5dd4)

~~~json
{
  "source": "00ae5dd4",
  "target": "00ae5e4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5ddc`](#insn-00ae5ddc)

~~~json
{
  "source": "00ae5ddc",
  "target": "010a03e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5de4`](#insn-00ae5de4)

~~~json
{
  "source": "00ae5de4",
  "target": "00ae5dfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5df8`](#insn-00ae5df8)

~~~json
{
  "source": "00ae5df8",
  "target": "010a03e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5e10`](#insn-00ae5e10)

~~~json
{
  "source": "00ae5e10",
  "target": "00ae5e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5e38`](#insn-00ae5e38)

~~~json
{
  "source": "00ae5e38",
  "target": "010a03d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5e48`](#insn-00ae5e48)

~~~json
{
  "source": "00ae5e48",
  "target": "010a03d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5e4c`](#insn-00ae5e4c)

~~~json
{
  "source": "00ae5e4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5e50`](#insn-00ae5e50)

~~~json
{
  "source": "00ae5e50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
