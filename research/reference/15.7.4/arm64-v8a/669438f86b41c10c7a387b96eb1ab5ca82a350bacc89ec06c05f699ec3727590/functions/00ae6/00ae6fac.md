# 00ae6fac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae6f68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-78002e967516751c48e123a0036a0165)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b46d30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0056.md#compare-bfd8b0f0ca3cd870f5919588504ab357)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6fac",
  "name": "_ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "942644bd3e96fa64710246de7fc5f309463c2e47af2b52f43fe2a1950af7e8ac",
  "source_text_sha256": "942644bd3e96fa64710246de7fc5f309463c2e47af2b52f43fe2a1950af7e8ac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae6fac",
        "00ae7047"
      ]
    ],
    "bytes_sha256": "123aab1076ad1b9774fcffcf194d92b7d2c0edace261aedb0020f27b65797608",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 801 bytes

~~~c

bool _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a04f0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a04e8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7020 to 00be7023 has its CatchHandler @ 00ae8d68 */
                    /* try { // try from 00ae7024 to 00be70c7 has its CatchHandler @ 00ae6044 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a04f0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a04f0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae6fac"></a> `00ae6fac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae6fb0"></a> `00ae6fb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6fb4"></a> `00ae6fb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae6fb8"></a> `00ae6fb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae6fbc"></a> `00ae6fbc` | `d5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6fc0"></a> `00ae6fc0` | `a8 c2 53 39` | ldrb w8,[x21, #0x4f0] | `FALL_THROUGH`
<a id="insn-00ae6fc4"></a> `00ae6fc4` | `68 00 00 34` | cbz w8,0x00ae6fd0 | `CONDITIONAL_JUMP`
<a id="insn-00ae6fc8"></a> `00ae6fc8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ae6fcc"></a> `00ae6fcc` | `1b 00 00 14` | b 0x00ae7038 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae6fd0"></a> `00ae6fd0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ae6fd4"></a> `00ae6fd4` | `c9 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6fd8"></a> `00ae6fd8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00ae6fdc"></a> `00ae6fdc` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00ae6fe0"></a> `00ae6fe0` | `21 75 42 f9` | ldr x1,[x9, #0x4e8] | `FALL_THROUGH`
<a id="insn-00ae6fe4"></a> `00ae6fe4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00ae6fe8"></a> `00ae6fe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae6fec"></a> `00ae6fec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae6ff0"></a> `00ae6ff0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae6ff4"></a> `00ae6ff4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ae6ff8"></a> `00ae6ff8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae6ffc"></a> `00ae6ffc` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00ae7000"></a> `00ae7000` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7004"></a> `00ae7004` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00ae7008"></a> `00ae7008` | `20 01 00 54` | b.eq 0x00ae702c | `CONDITIONAL_JUMP`
<a id="insn-00ae700c"></a> `00ae700c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7010"></a> `00ae7010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7014"></a> `00ae7014` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00ae7018"></a> `00ae7018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae701c"></a> `00ae701c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7020"></a> `00ae7020` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7024"></a> `00ae7024` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00ae7028"></a> `00ae7028` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae702c"></a> `00ae702c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00ae7030"></a> `00ae7030` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00ae7034"></a> `00ae7034` | `a0 c2 13 39` | strb w0,[x21, #0x4f0] | `FALL_THROUGH`
<a id="insn-00ae7038"></a> `00ae7038` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae703c"></a> `00ae703c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7040"></a> `00ae7040` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae7044"></a> `00ae7044` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae6fac`](#insn-00ae6fac) 範囲 `[['00ae6fac', '00ae6fc7']]`
  - `CONDITIONAL_JUMP` [`00ae6fc4`](#insn-00ae6fc4) → [`00ae6fd0`](#insn-00ae6fd0)
  - `FALL_THROUGH` [`00ae6fc4`](#insn-00ae6fc4) → [`00ae6fc8`](#insn-00ae6fc8)
- ブロック [`00ae6fc8`](#insn-00ae6fc8) 範囲 `[['00ae6fc8', '00ae6fcf']]`
  - `UNCONDITIONAL_JUMP` [`00ae6fcc`](#insn-00ae6fcc) → [`00ae7038`](#insn-00ae7038)
- ブロック [`00ae6fd0`](#insn-00ae6fd0) 範囲 `[['00ae6fd0', '00ae700b']]`
  - `CONDITIONAL_JUMP` [`00ae7008`](#insn-00ae7008) → [`00ae702c`](#insn-00ae702c)
  - `FALL_THROUGH` [`00ae7008`](#insn-00ae7008) → [`00ae700c`](#insn-00ae700c)
- ブロック [`00ae700c`](#insn-00ae700c) 範囲 `[['00ae700c', '00ae701f']]`
  - `FALL_THROUGH` [`00ae701c`](#insn-00ae701c) → [`00ae7020`](#insn-00ae7020)
- ブロック [`00ae7020`](#insn-00ae7020) 範囲 `[['00ae7020', '00ae7023']]`
  - `FALL_THROUGH` [`00ae7020`](#insn-00ae7020) → [`00ae7024`](#insn-00ae7024)
- ブロック [`00ae7024`](#insn-00ae7024) 範囲 `[['00ae7024', '00ae702b']]`
  - `FALL_THROUGH` [`00ae7028`](#insn-00ae7028) → [`00ae702c`](#insn-00ae702c)
- ブロック [`00ae702c`](#insn-00ae702c) 範囲 `[['00ae702c', '00ae7037']]`
  - `FALL_THROUGH` [`00ae7034`](#insn-00ae7034) → [`00ae7038`](#insn-00ae7038)
- ブロック [`00ae7038`](#insn-00ae7038) 範囲 `[['00ae7038', '00ae7047']]`

## 命令位置別の参照

- [`00ae6fac`](#insn-00ae6fac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fb0`](#insn-00ae6fb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fb4`](#insn-00ae6fb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fc0`](#insn-00ae6fc0) → `010a04f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae6fc4`](#insn-00ae6fc4) → [`00ae6fd0`](#insn-00ae6fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fcc`](#insn-00ae6fcc) → [`00ae7038`](#insn-00ae7038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6fe0`](#insn-00ae6fe0) → `010a04e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7008`](#insn-00ae7008) → [`00ae702c`](#insn-00ae702c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7034`](#insn-00ae7034) → `010a04f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae7038`](#insn-00ae7038) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae703c`](#insn-00ae703c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae6fac`](#insn-00ae6fac)

~~~json
{
  "source": "00ae6fac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fb0`](#insn-00ae6fb0)

~~~json
{
  "source": "00ae6fb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fb4`](#insn-00ae6fb4)

~~~json
{
  "source": "00ae6fb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fc0`](#insn-00ae6fc0)

~~~json
{
  "source": "00ae6fc0",
  "target": "010a04f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6fc4`](#insn-00ae6fc4)

~~~json
{
  "source": "00ae6fc4",
  "target": "00ae6fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fcc`](#insn-00ae6fcc)

~~~json
{
  "source": "00ae6fcc",
  "target": "00ae7038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6fe0`](#insn-00ae6fe0)

~~~json
{
  "source": "00ae6fe0",
  "target": "010a04e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7008`](#insn-00ae7008)

~~~json
{
  "source": "00ae7008",
  "target": "00ae702c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7034`](#insn-00ae7034)

~~~json
{
  "source": "00ae7034",
  "target": "010a04f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7038`](#insn-00ae7038)

~~~json
{
  "source": "00ae7038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae703c`](#insn-00ae703c)

~~~json
{
  "source": "00ae703c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
