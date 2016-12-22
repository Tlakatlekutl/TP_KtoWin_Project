
$(function()
{
    var $from=$(".from");
    var $to=$(".to");
    var $fun=$(".fun");
    var $graph=$(".graph");
    var $button=$(".draw");
    var timerId = 0;

    $button.click(function(e)
    {
        e.preventDefault();
        var from = parseFloat($from.val());
        var to = parseFloat($to.val());
        var fun = ($fun.val());

        const points = [];
        var dx = 0.01;
        var interval = 10;
        var start = from;
        var end;

        for (var x = from; x <=to; x+=dx) {
          const y = eval(fun);
          points.push([x, y]);
        }
        $.plot($graph, [{ label: fun, data: points }], [points], {});
    })

});
