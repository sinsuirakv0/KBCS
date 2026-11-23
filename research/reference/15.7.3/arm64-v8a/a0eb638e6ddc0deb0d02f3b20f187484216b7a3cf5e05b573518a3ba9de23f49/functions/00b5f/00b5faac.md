# 00b5faac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b5f9e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f9e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0009.md#compare-f4bd5bb55f5cb33bff78addb81caffc4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5faf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5faf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-cb0986844b09b488be5b039601aac920)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5faac",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57092d213673760e8207ca96b662e375ad0cee67f2e5baabfac9bfdfa9879dda",
  "source_text_sha256": "57092d213673760e8207ca96b662e375ad0cee67f2e5baabfac9bfdfa9879dda",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5faac",
        "00b5fb27"
      ]
    ],
    "bytes_sha256": "cfd74b061b9640c2b3960b5da144d73b9d9eed28600d300bc76231aef02a7d1c",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddb60](../00bdd/00bddb60.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bde090](../00bde/00bde090.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0c30](../00be0/00be0c30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(long *param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
  FUN_00551e14(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_010a1438);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  lVar2 = *param_1;
  _ZN8firebase5Mutex7AcquireEv(lVar2 + 0x18);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,*param_1 + 0x200);
  _ZN8firebase5Mutex7ReleaseEv(lVar2 + 0x18);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5faac"></a> `00b5faac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5fab0"></a> `00b5fab0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fab4"></a> `00b5fab4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5fab8"></a> `00b5fab8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5fabc"></a> `00b5fabc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5fac0"></a> `00b5fac0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5fac4"></a> `00b5fac4` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00b5fac8"></a> `00b5fac8` | `ba f9 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5facc"></a> `00b5facc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5fad0"></a> `00b5fad0` | `09 2a 00 d0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5fad4"></a> `00b5fad4` | `22 1d 42 f9` | ldr x2,[x9, #0x438] | `FALL_THROUGH`
<a id="insn-00b5fad8"></a> `00b5fad8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5fadc"></a> `00b5fadc` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00b5fae0"></a> `00b5fae0` | `cd c8 e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fae4"></a> `00b5fae4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5fae8"></a> `00b5fae8` | `6a f9 01 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b5faec"></a> `00b5faec` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5faf0"></a> `00b5faf0` | `13 61 00 91` | add x19,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b5faf4"></a> `00b5faf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5faf8"></a> `00b5faf8` | `36 f8 01 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fafc"></a> `00b5fafc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5fb00"></a> `00b5fb00` | `02 01 08 91` | add x2,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00b5fb04"></a> `00b5fb04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5fb08"></a> `00b5fb08` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b5fb0c"></a> `00b5fb0c` | `49 04 02 94` | bl 0x00be0c30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fb10"></a> `00b5fb10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5fb14"></a> `00b5fb14` | `33 f8 01 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fb18"></a> `00b5fb18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5fb1c"></a> `00b5fb1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fb20"></a> `00b5fb20` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5fb24"></a> `00b5fb24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5faac`](#insn-00b5faac) 範囲 `[['00b5faac', '00b5fb27']]`

## 命令位置別の参照

- [`00b5faac`](#insn-00b5faac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fab0`](#insn-00b5fab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fab4`](#insn-00b5fab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fac8`](#insn-00b5fac8) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b5fad4`](#insn-00b5fad4) → `010a1438`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5fae0`](#insn-00b5fae0) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5fae8`](#insn-00b5fae8) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b5faf8`](#insn-00b5faf8) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00b5fb0c`](#insn-00b5fb0c) → [`00be0c30`](../00be0/00be0c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0c30` · 推定シンボル `None` · 推定型 `None`
- [`00b5fb14`](#insn-00b5fb14) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00b5fb18`](#insn-00b5fb18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fb1c`](#insn-00b5fb1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5faac`](#insn-00b5faac)

~~~json
{
  "source": "00b5faac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fab0`](#insn-00b5fab0)

~~~json
{
  "source": "00b5fab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fab4`](#insn-00b5fab4)

~~~json
{
  "source": "00b5fab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fac8`](#insn-00b5fac8)

~~~json
{
  "source": "00b5fac8",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fad4`](#insn-00b5fad4)

~~~json
{
  "source": "00b5fad4",
  "target": "010a1438",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1438",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5fae0`](#insn-00b5fae0)

~~~json
{
  "source": "00b5fae0",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fae8`](#insn-00b5fae8)

~~~json
{
  "source": "00b5fae8",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5faf8`](#insn-00b5faf8)

~~~json
{
  "source": "00b5faf8",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fb0c`](#insn-00b5fb0c)

~~~json
{
  "source": "00b5fb0c",
  "target": "00be0c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fb14`](#insn-00b5fb14)

~~~json
{
  "source": "00b5fb14",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fb18`](#insn-00b5fb18)

~~~json
{
  "source": "00b5fb18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fb1c`](#insn-00b5fb1c)

~~~json
{
  "source": "00b5fb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
