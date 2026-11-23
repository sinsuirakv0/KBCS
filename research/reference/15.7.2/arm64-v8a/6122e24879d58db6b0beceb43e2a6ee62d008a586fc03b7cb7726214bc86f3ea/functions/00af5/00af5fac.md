# 00af5fac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af6074`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-34e34724fa6ee2107e48e8d7b1e5f377)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5fac",
  "name": "_ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02ac5efe381d4f01ce8780b12600580e01a0281f66e74f02418f33b1382cff1d",
  "source_text_sha256": "02ac5efe381d4f01ce8780b12600580e01a0281f66e74f02418f33b1382cff1d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5fac",
        "00af6023"
      ]
    ],
    "bytes_sha256": "cbd8f4e3ec8747fde9f24e6c7a8c7725e633b1c837ab3e088882e5d76e81d97a",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde260](../00bde/00bde260.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 855 bytes

~~~c

void _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv(long param_1)

{
  char cVar1;
  long *plVar2;
  
  plVar2 = (long *)_ZNK8firebase8internal16JObjectReference9GetJNIEnvEv();
  if (*(long *)(param_1 + 8) != 0) {
    FUN_00551e14(plVar2,*(long *)(param_1 + 8),DAT_010a02d8);
    cVar1 = (**(code **)(*plVar2 + 0x720))(plVar2);
    if (cVar1 != '\0') {
                    /* try { // try from 00af5ff0 to 00bf5ff7 has its CatchHandler @ 00affb08 */
      (**(code **)(*plVar2 + 0x80))(plVar2);
                    /* try { // try from 00af6000 to 00bf6007 has its CatchHandler @ 00affb00 */
                    /* WARNING: Could not recover jumptable at 0x00af6014. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar2 + 0x88))(plVar2);
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5fac"></a> `00af5fac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af5fb0"></a> `00af5fb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5fb4"></a> `00af5fb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af5fb8"></a> `00af5fb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af5fbc"></a> `00af5fbc` | `a9 a0 03 94` | bl 0x00bde260 | `UNCONDITIONAL_CALL`
<a id="insn-00af5fc0"></a> `00af5fc0` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af5fc4"></a> `00af5fc4` | `a1 02 00 b4` | cbz x1,0x00af6018 | `CONDITIONAL_JUMP`
<a id="insn-00af5fc8"></a> `00af5fc8` | `48 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5fcc"></a> `00af5fcc` | `02 6d 41 f9` | ldr x2,[x8, #0x2d8] | `FALL_THROUGH`
<a id="insn-00af5fd0"></a> `00af5fd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af5fd4"></a> `00af5fd4` | `90 6f e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00af5fd8"></a> `00af5fd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5fdc"></a> `00af5fdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5fe0"></a> `00af5fe0` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af5fe4"></a> `00af5fe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5fe8"></a> `00af5fe8` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af5fec"></a> `00af5fec` | `60 01 00 54` | b.eq 0x00af6018 | `CONDITIONAL_JUMP`
<a id="insn-00af5ff0"></a> `00af5ff0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5ff4"></a> `00af5ff4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5ff8"></a> `00af5ff8` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af5ffc"></a> `00af5ffc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af6000"></a> `00af6000` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af6004"></a> `00af6004` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6008"></a> `00af6008` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af600c"></a> `00af600c` | `01 45 40 f9` | ldr x1,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af6010"></a> `00af6010` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6014"></a> `00af6014` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00af6018"></a> `00af6018` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af601c"></a> `00af601c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6020"></a> `00af6020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af5fac`](#insn-00af5fac) 範囲 `[['00af5fac', '00af5fc7']]`
  - `CONDITIONAL_JUMP` [`00af5fc4`](#insn-00af5fc4) → [`00af6018`](#insn-00af6018)
  - `FALL_THROUGH` [`00af5fc4`](#insn-00af5fc4) → [`00af5fc8`](#insn-00af5fc8)
- ブロック [`00af5fc8`](#insn-00af5fc8) 範囲 `[['00af5fc8', '00af5fef']]`
  - `CONDITIONAL_JUMP` [`00af5fec`](#insn-00af5fec) → [`00af6018`](#insn-00af6018)
  - `FALL_THROUGH` [`00af5fec`](#insn-00af5fec) → [`00af5ff0`](#insn-00af5ff0)
- ブロック [`00af5ff0`](#insn-00af5ff0) 範囲 `[['00af5ff0', '00af5fff']]`
  - `FALL_THROUGH` [`00af5ffc`](#insn-00af5ffc) → [`00af6000`](#insn-00af6000)
- ブロック [`00af6000`](#insn-00af6000) 範囲 `[['00af6000', '00af6017']]`
- ブロック [`00af6018`](#insn-00af6018) 範囲 `[['00af6018', '00af6023']]`

## 命令位置別の参照

- [`00af5fac`](#insn-00af5fac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fb0`](#insn-00af5fb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fbc`](#insn-00af5fbc) → [`00bde260`](../00bde/00bde260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde260` · 推定シンボル `None` · 推定型 `None`
- [`00af5fc4`](#insn-00af5fc4) → [`00af6018`](#insn-00af6018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fcc`](#insn-00af5fcc) → `010a02d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af5fd4`](#insn-00af5fd4) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00af5fec`](#insn-00af5fec) → [`00af6018`](#insn-00af6018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6004`](#insn-00af6004) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6018`](#insn-00af6018) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5fac`](#insn-00af5fac)

~~~json
{
  "source": "00af5fac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fb0`](#insn-00af5fb0)

~~~json
{
  "source": "00af5fb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fbc`](#insn-00af5fbc)

~~~json
{
  "source": "00af5fbc",
  "target": "00bde260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5fc4`](#insn-00af5fc4)

~~~json
{
  "source": "00af5fc4",
  "target": "00af6018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fcc`](#insn-00af5fcc)

~~~json
{
  "source": "00af5fcc",
  "target": "010a02d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a02d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af5fd4`](#insn-00af5fd4)

~~~json
{
  "source": "00af5fd4",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5fec`](#insn-00af5fec)

~~~json
{
  "source": "00af5fec",
  "target": "00af6018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6004`](#insn-00af6004)

~~~json
{
  "source": "00af6004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6018`](#insn-00af6018)

~~~json
{
  "source": "00af6018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
