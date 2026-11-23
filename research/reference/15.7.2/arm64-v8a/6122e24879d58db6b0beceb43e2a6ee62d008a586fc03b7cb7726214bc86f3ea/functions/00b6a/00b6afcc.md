# 00b6afcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6b094`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-94472ea2a0c8b8aa8c2a5647d07f8c59)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6afcc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f456947af486f0c6c6ff6cd0df263c6609dbcd1ac3b1e78d19c92cc1113c79b4",
  "source_text_sha256": "f456947af486f0c6c6ff6cd0df263c6609dbcd1ac3b1e78d19c92cc1113c79b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6afcc",
        "00b6b05b"
      ]
    ],
    "bytes_sha256": "e201dd83b050a2e4005858e0bf4522f57d4bce256e9b9543d22428870d5807e2",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bde080](../00bde/00bde080.md)
- [00bde100](../00bde/00bde100.md)
- [00bde2e0](../00bde/00bde2e0.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 614 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c1bb10 + 0x10);
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  FUN_00551e14(plVar2,*(undefined8 *)param_1[1],DAT_010a18c0);
  (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)param_1[1]);
  if ((void *)param_1[1] != (void *)0x0) {
    _ZdlPv((void *)param_1[1]);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6afcc"></a> `00b6afcc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6afd0"></a> `00b6afd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6afd4"></a> `00b6afd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6afd8"></a> `00b6afd8` | `88 05 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b6afdc"></a> `00b6afdc` | `08 89 45 f9` | ldr x8,[x8, #0xb10] | `FALL_THROUGH`
<a id="insn-00b6afe0"></a> `00b6afe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6afe4"></a> `00b6afe4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b6afe8"></a> `00b6afe8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6afec"></a> `00b6afec` | `bd cc 01 94` | bl 0x00bde2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6aff0"></a> `00b6aff0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6aff4"></a> `00b6aff4` | `80 00 00 b5` | cbnz x0,0x00b6b004 | `CONDITIONAL_JUMP`
<a id="insn-00b6aff8"></a> `00b6aff8` | `a0 b9 ff f0` | adrp x0,0x2a1000 | `FALL_THROUGH`
<a id="insn-00b6affc"></a> `00b6affc` | `00 fc 36 91` | add x0,x0,#0xdbf | `FALL_THROUGH`
<a id="insn-00b6b000"></a> `00b6b000` | `20 cc 01 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00b6b004"></a> `00b6b004` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6b008"></a> `00b6b008` | `3e cc 01 94` | bl 0x00bde100 | `UNCONDITIONAL_CALL`
<a id="insn-00b6b00c"></a> `00b6b00c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6b010"></a> `00b6b010` | `a9 29 00 d0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6b014"></a> `00b6b014` | `22 61 44 f9` | ldr x2,[x9, #0x8c0] | `FALL_THROUGH`
<a id="insn-00b6b018"></a> `00b6b018` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6b01c"></a> `00b6b01c` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00b6b020"></a> `00b6b020` | `7d 9b e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b6b024"></a> `00b6b024` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6b028"></a> `00b6b028` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00b6b02c"></a> `00b6b02c` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00b6b030"></a> `00b6b030` | `28 59 40 f9` | ldr x8,[x9, #0xb0] | `FALL_THROUGH`
<a id="insn-00b6b034"></a> `00b6b034` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6b038"></a> `00b6b038` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b6b03c"></a> `00b6b03c` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6b040"></a> `00b6b040` | `80 00 00 b4` | cbz x0,0x00b6b050 | `CONDITIONAL_JUMP`
<a id="insn-00b6b044"></a> `00b6b044` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6b048"></a> `00b6b048` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6b04c"></a> `00b6b04c` | `c5 bf 01 14` | b 0x00bdaf60 | `CALL_TERMINATOR`
<a id="insn-00b6b050"></a> `00b6b050` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6b054"></a> `00b6b054` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6b058"></a> `00b6b058` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6afcc`](#insn-00b6afcc) 範囲 `[['00b6afcc', '00b6aff7']]`
  - `CONDITIONAL_JUMP` [`00b6aff4`](#insn-00b6aff4) → [`00b6b004`](#insn-00b6b004)
  - `FALL_THROUGH` [`00b6aff4`](#insn-00b6aff4) → [`00b6aff8`](#insn-00b6aff8)
- ブロック [`00b6aff8`](#insn-00b6aff8) 範囲 `[['00b6aff8', '00b6b003']]`
  - `FALL_THROUGH` [`00b6b000`](#insn-00b6b000) → [`00b6b004`](#insn-00b6b004)
- ブロック [`00b6b004`](#insn-00b6b004) 範囲 `[['00b6b004', '00b6b043']]`
  - `CONDITIONAL_JUMP` [`00b6b040`](#insn-00b6b040) → [`00b6b050`](#insn-00b6b050)
  - `FALL_THROUGH` [`00b6b040`](#insn-00b6b040) → [`00b6b044`](#insn-00b6b044)
- ブロック [`00b6b044`](#insn-00b6b044) 範囲 `[['00b6b044', '00b6b04f']]`
- ブロック [`00b6b050`](#insn-00b6b050) 範囲 `[['00b6b050', '00b6b05b']]`

## 命令位置別の参照

- [`00b6afcc`](#insn-00b6afcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afd0`](#insn-00b6afd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afdc`](#insn-00b6afdc) → `00c1bb10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b6afe8`](#insn-00b6afe8) → `00c12698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00b6afec`](#insn-00b6afec) → [`00bde2e0`](../00bde/00bde2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6aff4`](#insn-00b6aff4) → [`00b6b004`](#insn-00b6b004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6affc`](#insn-00b6affc) → `002a1dbf`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6b000`](#insn-00b6b000) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00b6b008`](#insn-00b6b008) → [`00bde100`](../00bde/00bde100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde100` · 推定シンボル `None` · 推定型 `None`
- [`00b6b014`](#insn-00b6b014) → `010a18c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6b020`](#insn-00b6b020) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b6b040`](#insn-00b6b040) → [`00b6b050`](#insn-00b6b050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6b044`](#insn-00b6b044) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6b04c`](#insn-00b6b04c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b6b050`](#insn-00b6b050) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6afcc`](#insn-00b6afcc)

~~~json
{
  "source": "00b6afcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afd0`](#insn-00b6afd0)

~~~json
{
  "source": "00b6afd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afdc`](#insn-00b6afdc)

~~~json
{
  "source": "00b6afdc",
  "target": "00c1bb10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bb10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b6afe8`](#insn-00b6afe8)

~~~json
{
  "source": "00b6afe8",
  "target": "00c12698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c12688",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b6afec`](#insn-00b6afec)

~~~json
{
  "source": "00b6afec",
  "target": "00bde2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6aff4`](#insn-00b6aff4)

~~~json
{
  "source": "00b6aff4",
  "target": "00b6b004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6affc`](#insn-00b6affc)

~~~json
{
  "source": "00b6affc",
  "target": "002a1dbf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1dbf",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002a1dbf",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b6b000`](#insn-00b6b000)

~~~json
{
  "source": "00b6b000",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6b008`](#insn-00b6b008)

~~~json
{
  "source": "00b6b008",
  "target": "00bde100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6b014`](#insn-00b6b014)

~~~json
{
  "source": "00b6b014",
  "target": "010a18c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a18c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6b020`](#insn-00b6b020)

~~~json
{
  "source": "00b6b020",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6b040`](#insn-00b6b040)

~~~json
{
  "source": "00b6b040",
  "target": "00b6b050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6b044`](#insn-00b6b044)

~~~json
{
  "source": "00b6b044",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6b04c`](#insn-00b6b04c)

~~~json
{
  "source": "00b6b04c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6b050`](#insn-00b6b050)

~~~json
{
  "source": "00b6b050",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
