# 00bdb9fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdaa08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-00a309f8badb57c49ad9bb2890f21683)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdb9fc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b66e6e0a8cdbb69f614b359eb1ba52b20ba1d3f52188938b9ad3797cf0384d6",
  "source_text_sha256": "9b66e6e0a8cdbb69f614b359eb1ba52b20ba1d3f52188938b9ad3797cf0384d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdb9fc",
        "00bdba8f"
      ]
    ],
    "bytes_sha256": "bc4d6e1a8e767e2037d8b1faa2f7da652ae573a9b6eefcbdaa524ed8fb94684f",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00589a54](../00589/00589a54.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 672 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev(long *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c9cae0 + 0x10);
  puVar1 = (undefined8 *)_Znwm(8);
  *puVar1 = 0;
  param_1[1] = (long)puVar1;
  lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar2 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
  uVar4 = FUN_00589a54(plVar3,DAT_01127d70,DAT_01127d80,param_1);
  uVar4 = (**(code **)(*plVar3 + 0xa8))(plVar3,uVar4);
  *(undefined8 *)param_1[1] = uVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdb9fc"></a> `00bdb9fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdba00"></a> `00bdba00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdba04"></a> `00bdba04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdba08"></a> `00bdba08` | `08 06 00 b0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bdba0c"></a> `00bdba0c` | `08 71 45 f9` | ldr x8,[x8, #0xae0] | `FALL_THROUGH`
<a id="insn-00bdba10"></a> `00bdba10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdba14"></a> `00bdba14` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdba18"></a> `00bdba18` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdba1c"></a> `00bdba1c` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdba20"></a> `00bdba20` | `44 f5 01 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdba24"></a> `00bdba24` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bdba28"></a> `00bdba28` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdba2c"></a> `00bdba2c` | `35 02 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdba30"></a> `00bdba30` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdba34"></a> `00bdba34` | `80 00 00 b5` | cbnz x0,0x00bdba44 | `CONDITIONAL_JUMP`
<a id="insn-00bdba38"></a> `00bdba38` | `a0 b6 ff f0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdba3c"></a> `00bdba3c` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdba40"></a> `00bdba40` | `98 01 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdba44"></a> `00bdba44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdba48"></a> `00bdba48` | `b6 01 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdba4c"></a> `00bdba4c` | `68 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdba50"></a> `00bdba50` | `69 2a 00 90` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdba54"></a> `00bdba54` | `01 b9 46 f9` | ldr x1,[x8, #0xd70] | `FALL_THROUGH`
<a id="insn-00bdba58"></a> `00bdba58` | `22 c1 46 f9` | ldr x2,[x9, #0xd80] | `FALL_THROUGH`
<a id="insn-00bdba5c"></a> `00bdba5c` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bdba60"></a> `00bdba60` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdba64"></a> `00bdba64` | `fc b7 e6 97` | bl 0x00589a54 | `UNCONDITIONAL_CALL`
<a id="insn-00bdba68"></a> `00bdba68` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdba6c"></a> `00bdba6c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdba70"></a> `00bdba70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdba74"></a> `00bdba74` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdba78"></a> `00bdba78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdba7c"></a> `00bdba7c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdba80"></a> `00bdba80` | `00 01 00 f9` | str x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdba84"></a> `00bdba84` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdba88"></a> `00bdba88` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdba8c"></a> `00bdba8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdb9fc`](#insn-00bdb9fc) 範囲 `[['00bdb9fc', '00bdba37']]`
  - `CONDITIONAL_JUMP` [`00bdba34`](#insn-00bdba34) → [`00bdba44`](#insn-00bdba44)
  - `FALL_THROUGH` [`00bdba34`](#insn-00bdba34) → [`00bdba38`](#insn-00bdba38)
- ブロック [`00bdba38`](#insn-00bdba38) 範囲 `[['00bdba38', '00bdba43']]`
  - `FALL_THROUGH` [`00bdba40`](#insn-00bdba40) → [`00bdba44`](#insn-00bdba44)
- ブロック [`00bdba44`](#insn-00bdba44) 範囲 `[['00bdba44', '00bdba8f']]`

## 命令位置別の参照

- [`00bdb9fc`](#insn-00bdb9fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdba00`](#insn-00bdba00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdba0c`](#insn-00bdba0c) → `00c9cae0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdba18`](#insn-00bdba18) → `00c935e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00bdba20`](#insn-00bdba20) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bdba2c`](#insn-00bdba2c) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdba34`](#insn-00bdba34) → [`00bdba44`](#insn-00bdba44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdba3c`](#insn-00bdba3c) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdba40`](#insn-00bdba40) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdba48`](#insn-00bdba48) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdba54`](#insn-00bdba54) → `01127d70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdba58`](#insn-00bdba58) → `01127d80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdba64`](#insn-00bdba64) → [`00589a54`](../00589/00589a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589a54` · 推定シンボル `None` · 推定型 `None`
- [`00bdba84`](#insn-00bdba84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdb9fc`](#insn-00bdb9fc)

~~~json
{
  "source": "00bdb9fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdba00`](#insn-00bdba00)

~~~json
{
  "source": "00bdba00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdba0c`](#insn-00bdba0c)

~~~json
{
  "source": "00bdba0c",
  "target": "00c9cae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cae0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdba18`](#insn-00bdba18)

~~~json
{
  "source": "00bdba18",
  "target": "00c935e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c935d0",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdba20`](#insn-00bdba20)

~~~json
{
  "source": "00bdba20",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdba2c`](#insn-00bdba2c)

~~~json
{
  "source": "00bdba2c",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdba34`](#insn-00bdba34)

~~~json
{
  "source": "00bdba34",
  "target": "00bdba44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdba3c`](#insn-00bdba3c)

~~~json
{
  "source": "00bdba3c",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdba40`](#insn-00bdba40)

~~~json
{
  "source": "00bdba40",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdba48`](#insn-00bdba48)

~~~json
{
  "source": "00bdba48",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdba54`](#insn-00bdba54)

~~~json
{
  "source": "00bdba54",
  "target": "01127d70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdba58`](#insn-00bdba58)

~~~json
{
  "source": "00bdba58",
  "target": "01127d80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127d80",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdba64`](#insn-00bdba64)

~~~json
{
  "source": "00bdba64",
  "target": "00589a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdba84`](#insn-00bdba84)

~~~json
{
  "source": "00bdba84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
